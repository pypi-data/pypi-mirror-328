"""
Module for the calculation of local sensitivities.
"""

import itertools
from typing import Dict, List, Union

import numpy as np
import plotly.graph_objs as go
import torch

from aixd.data.data_objects import DataCategorical, DataOrdinal, DataReal
from aixd.mlmodel.architecture.cond_ae_model import CondAEModel
from aixd.visualisation.styles import apply_default_style, color_qualitative10


class LocalSensitivity:
    """
    Sensitivity analysis class for the calculation of local sensitivities.

    Parameters
    ----------
    model: CondAEModel
        The LightningModule that defines the encoding process.
    """

    def __init__(self, model: CondAEModel) -> None:
        self.model = model

    def calculate(self, data: Union[torch.Tensor, Dict[str, torch.Tensor]], features: List[str] = None) -> Dict[str, np.ndarray]:
        """
        Calculate the local sensitivities by perfroming a sensitivity analysis
        of the output features with respect to the input features.
        For continous x features, the sensitivities are calculated as the
        gradients of y wrt x via backpropagation through the model.
        For categorical and ordinal x features the gradients are calculated
        as the finite difference (y(x')-y(x)).

        Parameters
        ----------
        data: torch.Tensor, dict(str, torch.Tensor)
            The data points at which the output sensitivity is calculated.
        features: list
            The list of ouptut features for which the sensitivity is
            calculated. If None, the sensitivity is calculated for all
            output features of the encoder.

        Returns
        -------
        sensitivity: dict
            The sensitivity of the output feature(s) with respect to the input.
        """

        if features is None:
            features = list(self.model.encoder.out_heads.keys())

        if isinstance(features, str):
            features = [features]

        sensitivity = {}

        for feature in features:

            if feature in self.model.encoder.out_heads.keys():
                if not isinstance(data, torch.Tensor):
                    raise TypeError("invalid data type")

                sensitivity[feature] = self._sensitivity_encoder(data, feature)

            elif feature in self.model.decoder.out_heads.keys():
                if not isinstance(data, dict):
                    raise TypeError("invalid data type")

                raise NotImplementedError

            else:
                raise ValueError("invalid feature name")

        return sensitivity

    def _sensitivity_encoder(self, data: torch.Tensor, feature: str) -> Dict[str, torch.Tensor]:
        """
        Calculate the sensitivity of a specific output feature of the encoder
        with respect to the encoder inputs.

        Parameters
        ----------
        data: torch.Tensor
            The input data to the encoder.
        feature: str
            The encoder output feature for which the sensitivity is calculated.

        Returns
        -------
        sensitivity: Dict[str, torch.Tensor]
            The dictionary of local sensitivities, in which the keys
            correspond to the encoder features and the values to the
            associated sensitivities.
        """

        # enable automatic differentiation
        if not data.requires_grad:
            data.requires_grad_(True)

        # ensure that the model is set to evaluation mode and predict output
        self.model.eval()
        output = self.model.encoder(data)

        # TODO: consider the case of categorical output feature

        position = self.model.decoder.splits[feature][0]
        output["y"][0, position].sum(axis=0).mean().backward(retain_graph=True)

        sensitivity_data = data.grad
        sensitivity = {}

        for dobj in self.model.input_ml_dblock.dobj_list:

            if dobj.name == feature:
                continue

            if isinstance(dobj, DataReal):
                position = self.model.encoder.splits[dobj.name][0]
                sensitivity[dobj.name] = sensitivity_data[0, position]

            elif isinstance(dobj, DataCategorical):
                noptions = len(dobj.domain.array)
                current_option = float(data[0, dobj.position_index])
                sensitivity[dobj.name] = {}

                for option in set(np.arange(noptions)) - {current_option}:
                    temp_data = data.detach().clone()
                    temp_data[:, dobj.position_index] = option

                    # get model prediction
                    temp_output = self.model.encoder(temp_data)
                    category = dobj.domain.array[option]

                    # calculate the sensitivity
                    diff = temp_output["y"] - output["y"]
                    sensitivity[dobj.name][category] = diff[0, position]

            elif isinstance(dobj, DataOrdinal):
                error = "sensitivity not implemented for ordinal data"
                raise NotImplementedError(error)

                # similar implementation with categoricals

            else:
                dtype = type(dobj)
                error = "sensitivity not implemented for {} data".format(dtype)
                raise NotImplementedError(error)

        # detach output tensors from the current graph
        output["y"].detach_()
        output["z"].detach_()

        return sensitivity

    def _get_xy_plot_data(self, sensitivity):
        """
        Extract the xy data to be used for the plot function.

        Parameters
        ----------
        sensitivity: dict
            The dictionary of local sensitivities.

        Returns
        -------
        x_data: list
            The x axis data values.
        y_data: list
            The y axis data labels.
        """

        x_data, y_data = [], []

        for key, value in sensitivity.items():
            if isinstance(value, dict):
                for key_, value_ in value.items():
                    x_data.append("{} {}".format(key, key_))
                    y_data.append(float(value_))
            else:
                x_data.append(key)
                y_data.append(float(value))

        return x_data, y_data

    def plot(self, data: Union[torch.Tensor, Dict[str, torch.Tensor]], features: List[str] = None, return_sens: bool = False) -> Dict[str, np.ndarray]:
        """
        Plot the local sensitivities for a specific feature in a horizontal
        bar chart.

        Parameters
        ----------
        data: torch.Tensor
            The input data at which the sensitivities are calculated.
        feature: str
            The feature for which the sensitivity is calculated.
        return_sens: Bool, False
            A boolean determining if the calculated sensitivities are returned.

        Returns
        -------
        sensitivity: dict
            The dictionary of local sensitivities.
        """

        if features is None:
            features = list(self.model.encoder.out_heads.keys())

        if isinstance(features, str):
            features = [features]

        sensitivity = self.calculate(data, features)

        for feature in features:
            fsensitivity = sensitivity[feature]

            fig = go.Figure()

            # data preparation
            x_data, y_data = self._get_xy_plot_data(fsensitivity)

            # data plotting
            fig.add_trace(
                go.Bar(
                    x=y_data,
                    y=x_data,
                    marker=dict(
                        color=color_qualitative10,
                        line=dict(color=color_qualitative10, width=1),
                    ),
                    name="Local Sensitivity",
                    orientation="h",
                )
            )

            fig.update_layout(
                title="Local Sensitivity of {}".format(feature),
                yaxis=dict(
                    title="Design Parameters",
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                ),
                xaxis=dict(
                    title="Sensitivity",
                    zeroline=False,
                    showline=False,
                    showticklabels=True,
                    showgrid=True,
                ),
            )
            fig.add_shape(type="line", x0=0, y0=0, x1=0, y1=1, xref="x", yref="paper", line=dict(color="black", width=1))
            apply_default_style(fig)
            fig.show()

        if return_sens:
            return sensitivity


class GlobalSensitivity:
    """
    Sensitivity analysis class for the calculation of global sensitivities.

    Parameters
    ----------
    model: CondAEModel
        The LightningModule that defines the encoding process.
    """

    def __init__(self, model: CondAEModel) -> None:
        self.model = model
        self._local = LocalSensitivity(model)

    def calculate(self, data: Union[torch.Tensor, Dict[str, torch.Tensor]], features: List[str] = None) -> Dict[str, np.ndarray]:
        """
        Calculate the global sensitivities by perfroming a sensitivity analysis
        of the output features with respect to the input features.
        For continous x features, the sensitivities are calculated as the
        gradients of y wrt x via backpropagation through the model.
        For categorical and ordinal x features the gradients are calculated
        as the finite difference (y(x')-y(x)).

        Parameters
        ----------
        data: torch.Tensor, dict(str, torch.Tensor)
            The data points at which the output sensitivity is calculated.
        features: List[str]
            The list of output features for which the sensitivity is
            calculated. If None, the sensitivity is calculated for all
            output features of the encoder.

        Returns
        -------
        sensitivity: dict
            The sensitivity of the output feature(s) with respect to the input.
        """

        if features is None:
            features = list(self.model.encoder.out_heads.keys())

        if isinstance(features, str):
            features = [features]

        sensitivity = {}

        for feature in features:
            sensitivity_list = []

            # calculate local sensitivities for each data point
            for data_point in data:
                data_ = data_point.view(1, -1).detach().requires_grad_(True)
                local_sensitivity = self._local.calculate(data_, feature)
                sensitivity_list.append(local_sensitivity)

            # aggregate the sensitivities
            dict_keys = sensitivity_list[0][feature].keys()
            sensitivity[feature] = dict.fromkeys(dict_keys)

            for key in sensitivity[feature].keys():
                # sensitivity wrt discrete (categorical, ordinal, etc) variables
                if isinstance(sensitivity_list[0][feature][key], dict):
                    keys = [tuple(item[feature][key].keys()) for item in sensitivity_list]
                    keys = sorted(list(set(itertools.chain.from_iterable(keys))))
                    sensitivity[feature][key] = dict.fromkeys(keys)

                    for sub_key in keys:
                        sub_key_grads = []
                        for item in sensitivity_list:
                            try:
                                sub_key_grads.append(item[feature][key][sub_key])
                            except KeyError:
                                pass

                        sensitivity[feature][key][sub_key] = torch.stack(sub_key_grads, dim=-1)
                # sensitivity wrt to continuous variables
                else:
                    key_sens = [item[feature][key] for item in sensitivity_list]
                    sensitivity[feature][key] = torch.stack(key_sens, dim=0)

        return sensitivity

    def plot(self, data: Union[torch.Tensor, Dict[str, torch.Tensor]], features: List[str], return_sens: bool = False) -> Dict[str, np.array]:
        """
        Plot the global sensitivities for a specific feature in a horizontal
        bar chart.

        Parameters
        ----------
        data: torch.Tensor
            The input data at which the sensitivity are calculated.
        features: str
            The list of feature(s) for which the sensitivity is calculated.
        return_sens: Bool, False
            A boolean determining if the calculated sensitivities are returned.

        Returns
        -------
        sensitivity: dict
            The dictionary of global sensitivities.
        """

        if features is None:
            features = list(self.model.encoder.out_heads.keys())

        if isinstance(features, str):
            features = [features]

        sensitivity = self.calculate(data, features)

        for feature in features:
            fsensitivity = sensitivity[feature]

            fig = go.Figure()
            # Use x instead of y argument for horizontal plot

            coloridx = 0
            for key, value in fsensitivity.items():
                if not isinstance(value, dict):
                    x_data = value.detach().numpy().flatten()
                    fig.add_trace(
                        go.Box(
                            x=x_data,
                            name=key,
                            boxpoints="all",
                            jitter=0.0,
                            whiskerwidth=0.5,
                            marker_size=2,
                            marker_color=color_qualitative10[coloridx],
                            line_width=1,
                        )
                    )
                    coloridx += 1

                else:
                    for subkey, subvalue in fsensitivity[key].items():
                        x_data = subvalue.detach().numpy().flatten()
                        if not isinstance(subkey, str):
                            subkey = str(subkey)

                        fig.add_trace(
                            go.Box(
                                x=x_data,
                                name=" ".join([key, subkey]),
                                boxpoints="all",
                                jitter=0.0,
                                whiskerwidth=0.5,
                                marker_size=2,
                                marker_color=color_qualitative10[coloridx],
                                line_width=1,
                            )
                        )
                        coloridx += 1

            fig.update_layout(
                title="Global Sensitivity of {}".format(feature),
                showlegend=False,
                yaxis=dict(
                    title="Design Parameters",
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                ),
                xaxis=dict(
                    title="Sensitivity",
                    zeroline=False,
                    showline=False,
                    showticklabels=True,
                    showgrid=True,
                ),
            )

            apply_default_style(fig)
            fig.show()

        if return_sens:
            return sensitivity
