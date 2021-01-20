import matplotlib
import matplotlib.pyplot as plt
# Read the rcParams file in the same figure
matplotlib.rc_file('publicationQualityFigures', use_default_template=True)

import numpy as np

# Main plotting routine
def main():

    ## ---------------------------------------------------------------------- ##
    ## IMPORT DATA
    # For files with no header, use numpy::loadtxt
    # flameT14 = np.loadtxt("r14_flame_t0000.50s.xy")

    # For files with a header, use numpy::genfromtxt for the ability to skip the
    # header lines 
    solidHtInfo = np.genfromtxt("./wallHeatFluxFlame.dat", skip_header=2)

    ## ---------------------------------------------------------------------- ##
    ## GENERATE FIGURE
    # Generate a figure and axes with subplot
    fig0 = plt.figure(figsize=(5, 7))
    ax0 = fig0.add_subplot(2, 1, 1)

    # Plot solid data
    ax0.plot(solidHtInfo[:, 0], -solidHtInfo[:, 4], label='$-$Solid')
    ax0.set_ylabel('Integrated Heat Flux [W]')

    # Populate additional subplot
    ax1 = fig0.add_subplot(2, 1, 2)
    ax1.plot(solidHtInfo[:, 0], -solidHtInfo[:, 2], '-.', marker="^", markerfacecolor='None', markevery=16, label='$-$Solid')
    ax1.set_xlabel('Time [sec]')
    ax1.set_ylabel('Heat Flux [W/m\\textsuperscript{2}]')

    ax0.minorticks_on()
    ax0.grid()
    ax1.minorticks_on()
    ax1.grid()
    ax0.legend(loc='upper right')
    fig0.tight_layout()

    # Display and then save the figure 
    plt.show()
    fig0.savefig(r'sampleFig.pdf', format='pdf', dpi=900)

if __name__ == '__main__':
    main()