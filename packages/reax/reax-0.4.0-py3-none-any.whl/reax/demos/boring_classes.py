import collections.abc
from typing import Any, Optional

from flax import linen
import jax
import jax.numpy as jnp
import numpy as np
import optax
from typing_extensions import override

from reax import data, modules

__all__ = "BoringModel", "RandomDataset"


class BoringModel(modules.Module):
    """Testing REAX Module.

    Use as follows:
    - subclass
    - modify the behavior for what you want

    .. warning::  This is meant for testing/debugging and is experimental.

    Example::

        class TestModel(BoringModel):
            def training_step(self, ...):
                ...  # do your own thing
    """

    def __init__(self) -> None:
        """Init function."""
        super().__init__()
        self.layer = linen.Dense(2)

    @override
    def setup(self, stage, batch: Any, /) -> None:
        """Setup function."""
        if self.parameters() is None:
            params = self.layer.init(self.rng_key(), batch[0])
            self.set_parameters(params)

    def forward(self, x: jax.Array) -> jax.Array:
        """Forward function."""
        return self.layer.apply(self.parameters(), x)

    def __call__(self, *args, **kwargs):
        """Call function."""
        return self.forward(*args, **kwargs)

    @staticmethod
    def loss(preds: jax.Array, labels: Optional[jax.Array] = None) -> jax.Array:
        """Loss function."""
        if labels is None:
            labels = jnp.ones_like(preds)
        # An arbitrary loss to have a loss that updates the model weights during `Trainer.fit` calls
        return optax.losses.squared_error(preds, labels).mean()

    @staticmethod
    def step(model: linen.Module, parameters, batch: Any) -> jax.Array:
        """Step function."""
        output = model.apply(parameters, batch)
        return BoringModel.loss(output)

    def training_step(self, batch: Any, batch_idx: int, /) -> Any:
        """Training step."""
        loss, grad = jax.value_and_grad(self.step, argnums=1)(self.layer, self.parameters(), batch)
        return {"loss": loss, "grad": grad}

    def validation_step(self, batch: Any, batch_idx: int, /) -> Any:
        """Validation step."""
        return {"x": self.step(self.layer, self.parameters(), batch)}

    def test_step(self, batch: Any, batch_idx: int, /) -> Any:
        """Test step."""
        return {"y": self.step(self.layer, self.parameters(), batch)}

    def predict_step(self, batch: Any, batch_idx: int, /) -> Any:
        """Predict step."""
        return self.forward(batch)

    def configure_optimizers(self) -> tuple:
        """Configure optimizers."""
        schedule = optax.exponential_decay(init_value=0.1, transition_steps=1, decay_rate=0.1)
        optimizer = optax.sgd(learning_rate=schedule)
        return optimizer, optimizer.init(self.parameters())

    def train_dataloader(self) -> data.DataLoader:
        """Train dataloader."""
        return data.ReaxDataLoader(RandomDataset(32, 64))

    def val_dataloader(self) -> data.DataLoader:
        """Val dataloader."""
        return data.ReaxDataLoader(RandomDataset(32, 64))

    def test_dataloader(self) -> data.DataLoader:
        """Test dataloader."""
        return data.ReaxDataLoader(RandomDataset(32, 64))

    def predict_dataloader(self) -> data.DataLoader:
        """Predict dataloader."""
        return data.ReaxDataLoader(RandomDataset(32, 64))


class RandomDataset(collections.abc.Sequence):
    """.. warning::  This is meant for testing/debugging and is experimental."""

    def __init__(self, size: int, length: int):
        self.len = length
        self.data = np.random.normal(size=(length, size))

    def __getitem__(self, index: int) -> jax.typing.ArrayLike:
        """Getitem function."""
        return self.data[index]

    def __len__(self) -> int:
        """Len function."""
        return self.len
