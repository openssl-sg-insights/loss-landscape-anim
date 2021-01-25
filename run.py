import numpy as np
from loss_landscape_anim import (
    loss_landscape_anim,
    MNISTDataModule,
    LeNet,
    compare_optimizers,
)


if __name__ == "__main__":
    optimizers = ["adam", "sgd", "adagrad", "rmsprop"]
    compare_optimizers(optimizers, param_count=603, train_new=False, seed=180224)

    # loss_landscape_anim(n_epochs=300)

    """
    u_gen = np.random.normal(size=61706)
    u = u_gen / np.linalg.norm(u_gen)
    v_gen = np.random.normal(size=61706)
    v = v_gen / np.linalg.norm(v_gen)

    bs = 16
    lr = 1e-3
    datamodule = MNISTDataModule(batch_size=bs, n_examples=3000)
    model = LeNet(learning_rate=lr)

    loss_landscape_anim(
        n_epochs=10,
        model=model,
        datamodule=datamodule,
        optimizer="adam",
        reduction_method="custom",
        custom_directions=(u, v),
        giffps=15,
        seed=180224,
        load_model=False,
        output_to_file=True,
        gpus=0,  # Set to # gpus if available
    )
    """
