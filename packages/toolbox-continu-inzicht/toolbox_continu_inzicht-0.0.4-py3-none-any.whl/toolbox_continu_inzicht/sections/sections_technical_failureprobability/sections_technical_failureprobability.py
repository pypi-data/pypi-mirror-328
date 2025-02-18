"""
Bepaal de technische faalkans van een dijkvak
"""

from pydantic.dataclasses import dataclass
from scipy.interpolate import interp1d
from toolbox_continu_inzicht.base.data_adapter import DataAdapter
from typing import Optional

import numpy as np
import pandas as pd


@dataclass(config={"arbitrary_types_allowed": True})
class SectionsTechnicalFailureprobability:
    """
    Bepaal de technische faalkans van een dijkvak

    ## Input schema's
    **input_schema_fragility_curves (DataFrame): schema voor fragility curves voor de dijkvak\n
    - section_id: int64                 : id van het dijkvak
    - failuremechanism: str             : code van het faalmechanisme
    - hydraulicload: float64            : belasting
    - failureprobability: float64       : faalkans

    **df_in_section_loads (DataFrame): schema voor tijdreeks met belasting op de dijkvak\n
    - section_id: int64                 : id van het dijkvak
    - parameter_id: int64               : id van de belastingparameter (1,2,3,4)
    - unit: str                         : eenheid van de belastingparameter
    - date_time: datetime64[ns, UTC]    : datum/ tijd van de tijdreeksitem
    - value: float64                    : belasting van de tijdreeksitem
    - value_type: str                   : type waarde van de tijdreeksitem (meting of verwacht)

    ## Output schema
    **df_out (DataFrame): uitvoer\n
    - section_id: int64                 : id van het dijkvak
    - parameter_id: int64               : id van de faalkans parameter (5,100,101,102)
    - unit: str                         : eenheid van de belastingparameter
    - date_time: datetime64[ns, UTC]    : datum/ tijd van de tijdreeksitem
    - value: float64                    : belasting van de tijdreeksitem
    - value_type: str                   : type waarde van de tijdreeksitem (meting of verwacht)
    - failureprobability float64        : faalkans bepaald voor de tijdreeksitem
    - failuremechanism: str             : code van het faalmechanisme
    """

    data_adapter: DataAdapter

    df_in_section_loads: Optional[pd.DataFrame] | None = None
    """DataFrame: tijdreeks met belasting op de dijkvak."""

    df_in_fragility_curves: Optional[pd.DataFrame] | None = None
    """DataFrame: fragility curves voor de dijkvak."""

    df_out: Optional[pd.DataFrame] | None = None
    """DataFrame: uitvoer."""

    # fragility curve per dijkvak
    input_schema_fragility_curves = {
        "section_id": "int64",
        "failuremechanism": "object",
        "hydraulicload": "float64",
        "failureprobability": "float64",
    }

    # belasting per moment per dijkvak
    input_schema_loads = {
        "section_id": "int64",
        "parameter_id": "int64",
        "unit": "object",
        "date_time": ["datetime64[ns, UTC]", "object"],
        "value": "float64",
        "value_type": "object",
    }

    def run(self, input: list[str], output: str) -> None:
        """
        Uitvoeren van het bepalen van de faalkans van een dijkvak.

        Args:\n
            input (list[str]): Lijst met namen van configuratie:
                [0] tijdreeks met belasting op de dijkvak
                [1] fragility curves voor de dijkvak
            output (str): uitvoer sectie van het yaml-bestand.
        """

        if not len(input) == 2:
            raise UserWarning(
                "Input variabele moet 2 string waarden bevatten. (fragility curve per dijkvak/belasting per dijkvak)"
            )

        # invoer 1: fragility curve per dijkvak per faalmechanisme
        self.df_in_fragility_curves = self.data_adapter.input(
            input[0], self.input_schema_fragility_curves
        )

        # invoer 2: belasting per dijkvak
        self.df_in_belasting = self.data_adapter.input(
            input[1], self.input_schema_loads
        )

        # Datum als string omzetten naar datetime object
        if not pd.api.types.is_datetime64_any_dtype(self.df_in_belasting["date_time"]):
            self.df_in_belasting["date_time"] = pd.to_datetime(
                self.df_in_belasting["date_time"]
            )

        # uitvoer: belasting per dijkvak
        self.df_out = pd.DataFrame()

        # Unieke combinaties van section_id en failuremechanism
        unique_combinations = (
            self.df_in_fragility_curves[["section_id", "failuremechanism"]]
            .drop_duplicates(subset=["section_id", "failuremechanism"])
            .reset_index(drop=True)
        )

        for _, combination in unique_combinations.iterrows():
            section_id = combination["section_id"]
            failuremechanism = combination["failuremechanism"]

            # Filter de DataFrames
            filtered_df_values = self.df_in_belasting[
                self.df_in_belasting["section_id"] == section_id
            ].copy()
            filtered_df_fragility_curves = self.df_in_fragility_curves[
                (self.df_in_fragility_curves["section_id"] == section_id)
                & (self.df_in_fragility_curves["failuremechanism"] == failuremechanism)
            ].copy()

            # Vervang nulwaarden door een kleine positieve waarde
            small_positive_value = 1e-10
            filtered_df_fragility_curves["failureprobability"] = (
                filtered_df_fragility_curves["failureprobability"].replace(
                    0, small_positive_value
                )
            )

            x_unique, unique_indices = np.unique(
                filtered_df_fragility_curves["hydraulicload"], return_index=True
            )
            y_unique = filtered_df_fragility_curves["failureprobability"].iloc[
                unique_indices
            ]

            # Logaritmische interpolatie en extrapolatie functie voor failureprobability
            log_interp_func = interp1d(
                x_unique,
                np.log(y_unique),
                fill_value="extrapolate",  # type: ignore
            )

            # Toepassen van logaritmische interpolatie en extrapolatie
            log_failureprobability = log_interp_func(filtered_df_values["value"])
            filtered_df_values["failureprobability"] = np.exp(log_failureprobability)

            # Voeg de failuremechanism kolom toe
            filtered_df_values["failuremechanism"] = failuremechanism

            # Vervang kleine positieve waarde door een 0
            # TODO RW is het nodig om de kans terug te zetten naar 0.0?
            # filtered_df_values['failureprobability'] = filtered_df_values['failureprobability'].replace(small_positive_value, 0.0)

            # Voeg de gefilterde DataFrame toe aan de hoofd DataFrame
            self.df_out = pd.concat(
                [self.df_out, filtered_df_values], ignore_index=True
            )

        self.data_adapter.output(output=output, df=self.df_out)
