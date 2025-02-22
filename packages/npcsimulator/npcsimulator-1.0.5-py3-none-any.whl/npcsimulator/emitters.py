import numpy as np

def generate_measurements(emitter_position, poisson_mean, uncertainty_std):
    """
    Generates repeated measurements for each emitter, with uncertainty, optionally applying a membrane function.

    :param emitter_position: Numpy array of the emitter's true positions (N x 2 or N x 3).
    :param poisson_mean: Mean of the Poisson distribution for the number of measurements.
    :param uncertainty_std: Standard deviation of the Gaussian uncertainty.

    :return: Numpy array of repeated measurements (M x 2 or M x 3).
    """
    emitter_position = np.atleast_2d(emitter_position)  # Ensure input is at least 2D
    new_emits = []

    for pos in emitter_position:
        # Generate random offsets
        num_measurements = np.random.poisson(poisson_mean)
        offsets = np.random.normal(loc=0, scale=uncertainty_std, size=(num_measurements, 2))
        measurements = pos + offsets
        new_emits.extend(measurements)

    return np.array(new_emits)



def dist_custom(centroids, Pe, Pf, radius, structures, abundances, gt_uncertainty=0,
                measured=7, ms_uncertainty=0.05):
    """
    Distributes emitters with user-provided structures, applying a membrane function if provided.

    :param centroids: List of centroid coordinates.
    :param Pe: Probability of emitter presence.
    :param Pf: Probability of fluorescence / signal received.
    :param radius: Radius of the centroid/emitter structures, enforces hard-core distance.
    :param structures: List of Numpy arrays representing structures ([structure1, structure2, ...]).
    :param abundances: List of abundances for each structure ([0.8, 0.2, ...]).
    :param gt_uncertainty: Uncertainty of ground truth emitters.
    :param measured: Poisson mean of the number of measurements per emitter.
    :param ms_uncertainty: Uncertainty of measurements around an emitter as a percentage of the radius.

    :return: Numpy arrays of labelled emitters, unlabelled emitters, and measurements.
    """
    labelled_emitters, unlabelled_emitters = [], []
    observed = []

    # Normalize abundance values
    abundances = np.array(abundances) / np.sum(abundances)

    if not structures or len(structures) == 0:
        raise ValueError("Structures list is empty or None.")
    if abundances is None or len(abundances) == 0:
        raise ValueError("Abundances list is empty or None.")
    if len(structures) != len(abundances):
        raise ValueError("Number of structures and abundances must match.")

    for centroid in centroids:
        # Select structure based on abundances
        structure_idx = np.random.choice(len(structures), p=abundances)
        structure = radius * structures[structure_idx]

        angle = np.random.uniform(0, 2*np.pi)
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                    [np.sin(angle), np.cos(angle)]])

        rotated_structure = (structure@rotation_matrix.T) + centroid

        # Process the points of the selected structure
        for point in rotated_structure:
            corrected_point = np.random.normal(loc=point, scale=gt_uncertainty) # Implement gt uncertainty
            if np.random.binomial(1, Pe):  # Biolabelling check
                labelled_emitters.append(corrected_point)
                measurements = generate_measurements(corrected_point, poisson_mean=measured,
                                                     uncertainty_std=ms_uncertainty*radius)
                for measurement in measurements:
                    if np.random.binomial(1, Pf):  # Signal received check
                        observed.append(measurement)
                    else:
                        continue
            else:
                unlabelled_emitters.append(corrected_point)

    return (np.array(labelled_emitters), np.array(unlabelled_emitters),
            np.array(observed))



def gen_noise(xrange, yrange, rho, measured=5, ms_uncertainty=0.5):
    """
    Generates random noise emitters across the specified window area (2D or 3D).

    :param xrange: Tuple specifying the (min, max) x-coordinate bounds for the window.
    :param yrange: Tuple specifying the (min, max) y-coordinate bounds for the window.
    :param rho: Poisson mean of number of noise clusters to be generated.
    :param measured: Poisson mean of number of measurements around noise emitter.
    :param ms_uncertainty: Uncertainty of measurement position around the noise emitter.

    :return: Array of noise emitter coordinates (2D or 3D).
    """
    n_noise_emitters = np.random.poisson(rho)

    # Generate the 2D noise for x and y coordinates
    x_noise = np.random.uniform(xrange[0], xrange[1], n_noise_emitters)
    y_noise = np.random.uniform(yrange[0], yrange[1], n_noise_emitters)

    # If a membrane function is provided, make noise 3D
    noise = np.column_stack((x_noise, y_noise))
    clutter = []
    for point in noise:
        measurements = generate_measurements(point, poisson_mean=measured, uncertainty_std=ms_uncertainty)
        for measurement in measurements:
            clutter.append(measurement)

    return np.array(clutter)