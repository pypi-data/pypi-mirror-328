from pathlib import Path
import nibabel
import dataclasses
import numpy as np
import numpy.typing as npt
import re
from typing import Optional


@dataclasses.dataclass
class SimpleMRI:
    data: np.ndarray
    affine: np.ndarray

    def __getitem__(self, key):
        return self.data[key]

    @property
    def shape(self) -> tuple[int, ...]:
        return self.data.shape


def apply_affine(T: np.ndarray, X: np.ndarray) -> np.ndarray:
    """Apply homogeneous-coordinate affine matrix T to each row of of matrix
    X of shape (N, 3)"""
    A = T[:-1, :-1]
    b = T[:-1, -1]
    return A.dot(X.T).T + b


def data_reorientation(mri: SimpleMRI) -> SimpleMRI:
    """Reorients the data-array and affine map such that the affine map is
    closest to the identity-matrix, such that increasing the first index
    corresponds to increasing the first coordinate in real space, and so on.

    The target coordinate system is still the same (i.e. RAS stays RAS)
    """
    A = mri.affine[:3, :3]
    flips = np.sign(A[np.argmax(np.abs(A), axis=0), np.arange(3)]).astype(int)
    permutes = np.argmax(np.abs(A), axis=0)
    offsets = ((1 - flips) // 2) * (np.array(mri.data.shape[:3]) - 1)

    # Index flip matrix
    F = np.eye(4, dtype=int)
    F[:3, :3] = np.diag(flips)
    F[:3, 3] = offsets

    # Index permutation matrix
    P = np.eye(4, dtype=int)[[*permutes, 3]]
    T = mri.affine @ F @ P

    inverse_permutes = np.argmax(P[:3, :3].T, axis=1)
    data = (
        mri.data[:: flips[0], :: flips[1], :: flips[2], ...]
        .transpose([*inverse_permutes, *list(range(3, mri.data.ndim))])
        .copy()
    )
    return SimpleMRI(data, T)


def change_of_coordinates_map(orientation_in: str, orientation_out: str) -> np.ndarray:
    """Creates an affine map for change of coordinate system based on the
    string identifiers
     L(eft) <-> R(ight)
     P(osterior) <-> A(nterior)
     I(nferior) <-> S(uperior)
    change of coordinate system affine map"""
    axes_labels = {
        "R": 0,
        "L": 0,
        "A": 1,
        "P": 1,
        "S": 2,
        "I": 2,
    }
    order = np.nan * np.empty(len(orientation_in))
    for idx1, char1 in enumerate(orientation_in):
        if char1 not in axes_labels:
            raise ValueError(f"'{char1}' not a valid axis label")

        # Start indexing at 1 to avoid 0 in the sign-function.
        for idx2, char2 in enumerate(orientation_out, start=1):
            if char2 not in axes_labels:
                raise ValueError(f"'{char2}' not a valid axis label")
            if axes_labels[char1] == axes_labels[char2]:
                if char1 == char2:
                    order[idx1] = idx2
                else:
                    order[idx1] = -idx2
                break

            if idx2 == len(orientation_out):
                print(char1, char2)
                raise ValueError(
                    f"Couldn't find axis in '{orientation_out}' corresponding to '{char1}'"
                )
    index_flip = np.sign(order).astype(int)
    index_order = np.abs(order).astype(int) - 1  # Map back to 0-indexing

    F = np.eye(4)
    F[:3, :3] = np.diag(index_flip)

    P = np.eye(4)
    P[:, :3] = P[:, index_order]
    return P @ F


def load_mri(
    path: Path | str,
    dtype: type,
    orient: bool = True,
) -> SimpleMRI:
    suffix_regex = re.compile(r".+(?P<suffix>(\.nii(\.gz|)|\.mg(z|h)))")
    m = suffix_regex.match(Path(path).name)
    if (m is not None) and (m.groupdict()["suffix"] in (".nii", ".nii.gz")):
        mri = nibabel.nifti1.load(path)
    elif (m is not None) and (m.groupdict()["suffix"] in (".mgz", ".mgh")):
        mri = nibabel.freesurfer.mghformat.load(path)
    else:
        raise ValueError(f"Invalid suffix {path}, should be either '.nii', or '.mgz'")

    affine = mri.affine
    if affine is None:
        raise RuntimeError("MRI do not contain affine")

    data = np.asarray(mri.get_fdata("unchanged"), dtype=dtype)
    mri = SimpleMRI(data=data, affine=affine)

    if orient:
        return data_reorientation(mri)
    else:
        return mri


def save_mri(
    mri: SimpleMRI, path: Path, dtype: npt.DTypeLike, intent_code: Optional[int] = None
):
    suffix_regex = re.compile(r".+(?P<suffix>(\.nii(\.gz|)|\.mg(z|h)))")
    m = suffix_regex.match(Path(path).name)
    if (m is not None) and (m.groupdict()["suffix"] in (".nii", ".nii.gz")):
        nii = nibabel.nifti1.Nifti1Image(mri.data.astype(dtype), mri.affine)
        if intent_code is not None:
            nii.header.set_intent(intent_code)
        nibabel.nifti1.save(nii, path)
    elif (m is not None) and (m.groupdict()["suffix"] in (".mgz", ".mgh")):
        mgh = nibabel.freesurfer.mghformat.MGHImage(mri.data.astype(dtype), mri.affine)
        if intent_code is not None:
            mgh.header.set_intent(intent_code)
        nibabel.freesurfer.mghformat.save(mgh, path)
    else:
        raise ValueError(f"Invalid suffix {path}, should be either '.nii', or '.mgz'")


def assert_same_space(mri1: SimpleMRI, mri2: SimpleMRI, rtol: float = 1e-5):
    if mri1.data.shape == mri1.data.shape and np.allclose(
        mri1.affine, mri2.affine, rtol
    ):
        return
    with np.printoptions(precision=5):
        raise ValueError(
            f"""MRI's not in same space (relative tolerance {rtol}).
            Shapes: ({mri1.data.shape}, {mri2.data.shape}),
            Affines: {mri1.affine}, {mri2.affine},
            Affine max relative error: {np.nanmax(np.abs((mri1.affine - mri2.affine) / mri2.affine))}"""
        )
