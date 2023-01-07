# Histogram implementation of a bayes filter - combines
# convolution and multiplication of distributions, for the
# movement and measurement steps.
# 06_d_histogram_filter
# Claus Brenner, 28 NOV 2012
from pylab import plot, show, ylim
from distribution import *

def move(distribution, delta):
    """Returns a Distribution that has been moved (x-axis) by the amount of
       delta."""
    return Distribution(distribution.offset + delta, distribution.values)

# --->>> Copy your convolve(a, b) and multiply(a, b) functions here.

def convolve(a, b):
    """Convolve distribution a and b and return the resulting new distribution."""

    distributions = []
    new_offset = a.offset + b.offset

    for a_value in a.values:
        values = []
        for b_value in b.values:
            values.append(a_value*b_value)
        distributions.append(Distribution(new_offset, values))
        new_offset += 1
    sum = Distribution.sum(distributions)

    return sum

def multiply(a, b):
    """Multiply two distributions and return the resulting distribution."""
    
    vals = []
    for i in range(min(a.start(), b.start()), max(a.stop(), b.stop()) + 1):
        vals.append((a.value(i) * b.value(i)))

    # Modify this to return your result.
    distribution = Distribution(min(a.offset, b.offset), vals)
    distribution.normalize()
    return distribution


if __name__ == '__main__':
    arena = (0, 220)

    # Start position. Exactly known - a unit pulse.
    start_position = 10
    position = Distribution.unit_pulse(start_position)
    plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
         drawstyle='steps')

    # Movement data.
    controls = [20] * 10

    # Measurement data. Assume (for now) that the measurement data
    # is correct. - This code just builds a cumulative list of the controls,
    # plus the start position.
    p = start_position
    measurements = []
    for c in controls:
        p += c
        measurements.append(p)

    # This is the filter loop.
    for i in range(len(controls)):
        # Move, by convolution. Also termed "prediction". # We loose information because of this step
        control = Distribution.triangle(controls[i], 10)
        position = convolve(control, position)
        plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             color='b', drawstyle='steps')

        # Measure, by multiplication. Also termed "correction". We gain information because of this step
        measurement = Distribution.triangle(measurements[i], 10)
        position = multiply(position, measurement)
        plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             color='r', drawstyle='steps')

    show()