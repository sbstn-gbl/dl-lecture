import matplotlib.pyplot as plt
import numpy as np
import torch
import yaml

plt.rcParams.update(
    {
        "figure.figsize": (10, 10),
        "axes.titlesize": 20,
        "axes.labelsize": 15,
        "legend.fontsize": 15,
        "axes.grid": True,
        "axes.axisbelow": True,
        "pcolor.shading": "auto",
    }
)


def yaml_load(f):
    with open(f, "r") as con:
        x = yaml.safe_load(con)
    return x


def yaml_save(x, f):
    with open(f, "w") as con:
        yaml.safe_dump(x, con)


def print_result(x, label):
    x = [xi.item() if torch.is_tensor(xi) else xi for xi in x]
    print(
        f"{label+':':9s} y = {x[0]:.2f} + {x[1]:.2f} x_1 + {x[2]:.2f} x_2 + {x[3]:.2f} x_3"
    )


def t2a(x):
    return x.detach().numpy()


def test(arr, tens, eps=1e-6):
    assert np.max(np.abs(arr - t2a(tens))) < eps


def score(x, y, trainer):

    p = trainer.predict(x).data.numpy()
    yhat = (p > 0.5).astype(int)

    accuracy = np.mean(y == yhat)
    average_precision = sklearn.metrics.average_precision_score(y, p)
    rocauc = sklearn.metrics.roc_auc_score(y, p)
    precision, recall, _ = sklearn.metrics.precision_recall_curve(y, p)
    prauc = sklearn.metrics.auc(recall, precision)

    xx = np.linspace(-20, 20, 400)
    yy = np.linspace(-20, 20, 400)
    gx, gy = np.meshgrid(xx, yy)
    Z = (
        trainer.predict(torch.tensor(np.c_[gx.ravel(), gy.ravel()].astype(np.float32)))
        .detach()
        .numpy()
        .reshape(gx.shape)
    )

    plt.contourf(gx, gy, Z, cmap=plt.cm.coolwarm, alpha=0.7)

    mask_11 = (y == 1) & (yhat == 1)
    mask_10 = (y == 1) & (yhat == 0)
    mask_00 = (y == 0) & (yhat == 0)
    mask_01 = (y == 0) & (yhat == 1)

    plt.scatter(
        x[mask_11, 0],
        x[mask_11, 1],
        s=100,
        c="darkred",
        marker="o",
        label="True Positive",
    )
    plt.scatter(
        x[mask_10, 0],
        x[mask_10, 1],
        s=100,
        c="darkred",
        marker="^",
        label="False Negative",
    )
    plt.scatter(
        x[mask_00, 0],
        x[mask_00, 1],
        s=100,
        c="darkblue",
        marker="o",
        label="True Negative",
    )
    plt.scatter(
        x[mask_01, 0],
        x[mask_01, 1],
        s=100,
        c="darkblue",
        marker="^",
        label="False Positive",
    )

    plt.title(
        f"acc={accuracy:.2f} | avg(prec)={average_precision:.2f} | rocauc={rocauc:.2f} | prauc={prauc:.2f}"
    )
    plt.xlabel(r"$x_1$")
    plt.ylabel(r"$x_2$")
    plt.legend(loc="upper left")
    plt.tight_layout()
