#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:21:12 2020

@author: elemhunt
"""
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------#
# CD Time Correction Vales
# Note: The First data point is always 'nan' so the correction value
#       must be input manually.
# ------------------------------------------------------------------------#

# Run 1
correction_val1_s1 = 1847.60876033524
correction_val1_s2 = 2000.79704594847
correction_val1_s3 = 1921.07805314974

# Run 2
correction_val2_s1 = 3846.00129528978
correction_val2_s2 = 2223.99244038496
correction_val2_s3 = 2916.68356563608

# Run 3
correction_val3_s1 = 4581.59870143258
correction_val3_s2 = 2252.78077131228
correction_val3_s3 = 3049.02881130194

# Run 4
correction_val4_s1 = 4741.82445302804
correction_val4_s2 = 2261.83870428941
correction_val4_s3 = 3071.83306624437

# # Run 5
# correction_val5_s1 =
# correction_val5_s2 =
# correction_val5_s3 =

# ------------------------------------------------------------------------#
# Load in Data
# Note: route of .txt files may need to be changes depending on directory
# ------------------------------------------------------------------------#

# Run 1
CV_r1_s1 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CV_0.005Vs_2C.txt')
CV_r1_s2 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S034/_CV_0.005Vs_2C.txt')
CV_r1_s3 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S035/_CV_0.005Vs_2C.txt')

CD_r1_s1 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CD_20e-6A_3C.txt')
CD_r1_s2 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S034/_CD_20e-6A_3C.txt')
CD_r1_s3 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S035/_CD_20e-6A_3C.txt')
# Run 2
CV_r2_s1 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CV_0.01Vs_2C.txt')
CV_r2_s2 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S034/_CV_0.01Vs_2C.txt')
CV_r2_s3 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S035/_CV_0.01Vs_2C.txt')

CD_r2_s1 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CD_50e-6A_3C.txt')
CD_r2_s2 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S034/_CD_50e-6A_3C.txt')
CD_r2_s3 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S035/_CD_50e-6A_3C.txt')

# # Run 3
CV_r3_s1 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CV_0.02Vs_2C.txt')
CV_r3_s2 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S034/_CV_0.02Vs_2C.txt')
CV_r3_s3 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S035/_CV_0.02Vs_2C.txt')

CD_r3_s1 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CD_100e-6A_3C.txt')
CD_r3_s2 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S034/_CD_100e-6A_3C.txt')
CD_r3_s3 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S035/_CD_100e-6A_3C.txt')

# # Run 4
CV_r4_s1 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CV_0.05Vs_2C.txt')
CV_r4_s2 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S034/_CV_0.05Vs_2C.txt')
CV_r4_s3 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S035/_CV_0.05Vs_2C.txt')

CD_r4_s1 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CD_200e-6A_3C.txt')
CD_r4_s2 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S034/_CD_200e-6A_3C.txt')
CD_r4_s3 = np.genfromtxt(
    '/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S035/_CD_200e-6A_3C.txt')

# # Run 5
# CV_r5_s1 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S024/_CV_0.5Vs_2C.txt')
# CV_r5_s2 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S022/_CV_0.5Vs_2C.txt')
# CV_r5_s3 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S022/_CV_0.5Vs_2C.txt')

# CD_r5_s1 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S024_CD_500e-6A_3C.txt')
# CD_r5_s2 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S022/_CD_500e-6A_3C.txt')
# CD_r5_s3 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S022/_CD_500e-6A_3C.txt')


# ------------------------------------------------------------------------#
# ------------------------------------------------------------------------#
# CV Comparisons
# ------------------------------------------------------------------------#
# ------------------------------------------------------------------------#


# ------------------------------------------------------------------------#
# Set Columns and Data Points
# ------------------------------------------------------------------------#

# Run 1
current_r1_s1 = CV_r1_s1[816:1638, 1]
voltage_r1_s1 = CV_r1_s1[816:1638, 2]

current_r1_s2 = CV_r1_s2[816:1638, 1]
voltage_r1_s2 = CV_r1_s2[816:1638, 2]

current_r1_s3 = CV_r1_s3[816:1638, 1]
voltage_r1_s3 = CV_r1_s3[816:1638, 2]

# Run 2
current_r2_s1 = CV_r2_s1[816:1638, 1]
voltage_r2_s1 = CV_r2_s1[816:1638, 2]

current_r2_s2 = CV_r2_s2[816:1638, 1]
voltage_r2_s2 = CV_r2_s2[816:1638, 2]

current_r2_s3 = CV_r2_s3[816:1638, 1]
voltage_r2_s3 = CV_r2_s3[816:1638, 2]

# Run 3
current_r3_s1 = CV_r3_s1[816:1638, 1]
voltage_r3_s1 = CV_r3_s1[816:1638, 2]

current_r3_s2 = CV_r3_s2[816:1638, 1]
voltage_r3_s2 = CV_r3_s2[816:1638, 2]

current_r3_s3 = CV_r3_s3[816:1638, 1]
voltage_r3_s3 = CV_r3_s3[816:1638, 2]

# Run 4
current_r4_s1 = CV_r4_s1[816:1638, 1]
voltage_r4_s1 = CV_r4_s1[816:1638, 2]

current_r4_s2 = CV_r4_s2[816:1638, 1]
voltage_r4_s2 = CV_r4_s2[816:1638, 2]

current_r4_s3 = CV_r4_s3[816:1638, 1]
voltage_r4_s3 = CV_r4_s3[816:1638, 2]

# # Run 5
# current_r5_s1 = CV_r5_s1[816:1638,1]
# voltage_r5_s1 = CV_r5_s1[816:1638,2]
# current_r5_s2 = CV_r5_s2[816:1638,1]
# voltage_r5_s2 = CV_r5_s2[816:1638,2]


# ------------------------------------------------------------------------#
# Plot
# Note: Legend and line color/width may need to be changed accrodingly
# ------------------------------------------------------------------------#

# Run 1
fig, ax1 = plt.subplots()
ax1.plot(voltage_r1_s1, current_r1_s1, 'g', linewidth=2.0)
ax1.plot(voltage_r1_s2, current_r1_s2, 'b', linewidth=2.0)
ax1.plot(voltage_r1_s3, current_r1_s3, 'm', linewidth=2.0)
ax1.legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})
ax1.set_title('CV - 0.005 V/s Comparison')
ax1.set_xlabel('Voltage (V)')
ax1.set_ylabel('Current (A)')

fig.savefig('0.005 Vs Comparions.png', dpi=1000)

# Run 2
fig, ax2 = plt.subplots()
ax2.plot(voltage_r2_s1, current_r2_s1, 'g', linewidth=2.0)
ax2.plot(voltage_r2_s2, current_r2_s2, 'b', linewidth=2.0)
ax2.plot(voltage_r2_s3, current_r2_s3, 'm', linewidth=2.0)
ax2.legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})
ax2.set_title('CV - 0.01 V/s Comparison')
ax2.set_xlabel('Voltage (V)')
ax2.set_ylabel('Current (A)')

fig.savefig('0.01 Vs Comparions.png', dpi=1000)

# Run 3
fig, ax3 = plt.subplots()
ax3.plot(voltage_r3_s1, current_r3_s1, 'g', linewidth=2.0)
ax3.plot(voltage_r3_s2, current_r3_s2, 'b', linewidth=2.0)
ax3.plot(voltage_r3_s3, current_r3_s3, 'm', linewidth=2.0)
ax3.legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})
ax3.set_title('CV - 0.02 V/s Comparison')
ax3.set_xlabel('Voltage (V)')
ax3.set_ylabel('Current (A)')

fig.savefig('0.02 Vs Comparions.png', dpi=1000)

# Run 4
fig, ax4 = plt.subplots()
ax4.plot(voltage_r4_s1, current_r4_s1, 'g', linewidth=2.0)
ax4.plot(voltage_r4_s2, current_r4_s2, 'b', linewidth=2.0)
ax4.plot(voltage_r4_s3, current_r4_s3, 'm', linewidth=2.0)
ax4.legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})
ax4.set_title('CV - 0.05 V/s Comparison')
ax4.set_xlabel('Voltage (V)')
ax4.set_ylabel('Current (A)')

fig.savefig('0.05 Vs Comparions.png', dpi=1000)

# # Run 5
# fig, ax5 = plt.subplots()
# ax5.plot(voltage_r5_s1,current_r5_s1,'g', linewidth=2.0)
# ax5.plot(voltage_r5_s2,current_r5_s2,'b', linewidth=2.0)
# ax5.legend(['No Vacuum','24 hr Vacuum'],loc='upper left', prop={'size': 7})
# ax5.set_title('CV - 0.5 Vs Comparison')
# ax5.set_xlabel('Voltage (V)')
# ax5.set_ylabel('Current (A)')

# fig.savefig('0.5 Vs Comparions.png', dpi = 1000)


# Plot all together (4x4)
fig, axs = plt.subplots(2, 2, gridspec_kw={'hspace': 0.4})

axs[0, 0].plot(voltage_r1_s1, current_r1_s1, 'g', linewidth=2.0)
axs[0, 0].plot(voltage_r1_s2, current_r1_s2, 'b', linewidth=2.0)
axs[0, 0].plot(voltage_r1_s3, current_r1_s3, 'm', linewidth=2.0)
axs[0, 0].set_title('(a)')
axs[0, 0].set_ylabel('Current (A)')
axs[0, 0].legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})

axs[0, 1].plot(voltage_r2_s1, current_r2_s1, 'g', linewidth=2.0)
axs[0, 1].plot(voltage_r2_s2, current_r2_s2, 'b', linewidth=2.0)
axs[0, 1].plot(voltage_r2_s3, current_r2_s3, 'm', linewidth=2.0)
axs[0, 1].set_title('(b)')
axs[0, 1].legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})

axs[1, 0].plot(voltage_r3_s1, current_r3_s1, 'g', linewidth=2.0)
axs[1, 0].plot(voltage_r3_s2, current_r3_s2, 'b', linewidth=2.0)
axs[1, 0].plot(voltage_r3_s3, current_r3_s3, 'm', linewidth=2.0)
axs[1, 0].set_title('(c)')
axs[1, 0].set_xlabel('Voltage (V)')
axs[1, 0].set_ylabel('Current (A)')
axs[1, 0].ticklabel_format(axis='y', style='sci', scilimits=(1, -5))
axs[1, 0].legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})

axs[1, 1].plot(voltage_r4_s1, current_r4_s1, 'g', linewidth=2.0)
axs[1, 1].plot(voltage_r4_s2, current_r4_s2, 'b', linewidth=2.0)
axs[1, 1].plot(voltage_r4_s3, current_r4_s3, 'm', linewidth=2.0)
axs[1, 1].ticklabel_format(axis='y', style='sci', scilimits=(1, -5))
axs[1, 1].set_title('(d)')
axs[1, 1].set_xlabel('Voltage (V)')
axs[1, 1].legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})

axs[0, 0].tick_params(axis='both', which='major', labelsize=5)
axs[0, 1].tick_params(axis='both', which='major', labelsize=5)
axs[1, 0].tick_params(axis='both', which='major', labelsize=5)
axs[1, 1].tick_params(axis='both', which='major', labelsize=5)

fig.savefig('CV S033 S034 S035 wired.png', dpi=1000)

# %%

# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#
# CD Comparisons
# --------------------------------------------------------------------------#
# --------------------------------------------------------------------------#


# ------------------------------------------------------------------------#
# Set Columns and Data Points
# ------------------------------------------------------------------------#

# Run 1

time1_s1 = CD_r1_s1[1:, 0]
fix_time1_s1 = time1_s1 - correction_val1_s1
voltage1_s1 = CD_r1_s1[1:, 2]

time1_s2 = CD_r1_s2[1:, 0]
fix_time1_s2 = time1_s2 - correction_val1_s2
voltage1_s2 = CD_r1_s2[1:, 2]

time1_s3 = CD_r1_s3[1:, 0]
fix_time1_s3 = time1_s3 - correction_val1_s3
voltage1_s3 = CD_r1_s3[1:, 2]

# Run 2

time2_s1 = CD_r2_s1[1:, 0]
fix_time2_s1 = time2_s1 - correction_val2_s1
voltage2_s1 = CD_r2_s1[1:, 2]

time2_s2 = CD_r2_s2[1:, 0]
fix_time2_s2 = time2_s2 - correction_val2_s2
voltage2_s2 = CD_r2_s2[1:, 2]

time2_s3 = CD_r2_s3[1:, 0]
fix_time2_s3 = time2_s3 - correction_val2_s3
voltage2_s3 = CD_r2_s3[1:, 2]

# Run 3

time3_s1 = CD_r3_s1[1:, 0]
fix_time3_s1 = time3_s1 - correction_val3_s1
voltage3_s1 = CD_r3_s1[1:, 2]

time3_s2 = CD_r3_s2[1:, 0]
fix_time3_s2 = time3_s2 - correction_val3_s2
voltage3_s2 = CD_r3_s2[1:, 2]

time3_s3 = CD_r3_s3[1:, 0]
fix_time3_s3 = time3_s3 - correction_val3_s3
voltage3_s3 = CD_r3_s3[1:, 2]

# Run 4

time4_s1 = CD_r4_s1[1:, 0]
fix_time4_s1 = time4_s1 - correction_val4_s1
voltage4_s1 = CD_r4_s1[1:, 2]

time4_s2 = CD_r4_s2[1:, 0]
fix_time4_s2 = time4_s2 - correction_val4_s2
voltage4_s2 = CD_r4_s2[1:, 2]

time4_s3 = CD_r4_s3[1:, 0]
fix_time4_s3 = time4_s3 - correction_val4_s3
voltage4_s3 = CD_r4_s3[1:, 2]

# # Run 5

# time5_s1 = CD_r5_s1 [1:,0]
# fix_time5_s1 = time5_s1 - correction_val5_s1
# voltage5_s1 = CD_r5_s1[1:,2]

# time5_s2 = CD_r5_s2 [1:,0]
# fix_time5_s2 = time5_s2 - correction_val5_s2
# voltage5_s2 = CD_r5_s2[1:,2]


# ------------------------------------------------------------------------#
# Plots
# Note: Legend and line color/width may need to be changed accrodingly
# ------------------------------------------------------------------------#

# Run 1
fig, bx1 = plt.subplots()
bx1.plot(fix_time1_s1, voltage1_s1, 'g', linewidth=2.0)
bx1.plot(fix_time1_s2, voltage1_s2, 'b', linewidth=2.0)
bx1.plot(fix_time1_s3, voltage1_s3, 'm', linewidth=2.0)
bx1.legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})
bx1.set_title('CD - 20e-6 A Comparison')
bx1.set_xlabel('Time (s)')
bx1.set_ylabel('Voltage (V)')

fig.savefig('CD - 20e-6 A Comparions.png', dpi=1000)

# Run 2
fig, bx2 = plt.subplots()
bx2.plot(fix_time2_s1, voltage2_s1, 'g', linewidth=2.0)
bx2.plot(fix_time2_s2, voltage2_s2, 'b', linewidth=2.0)
bx2.plot(fix_time2_s3, voltage2_s3, 'm', linewidth=2.0)
bx2.legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})
bx2.set_title('CD - 50e-6 A Comparison')
bx2.set_xlabel('Time (s)')
bx2.set_ylabel('Voltage (V)')

fig.savefig('CD - 50e-6 A Comparions.png', dpi=1000)

# Run 3
fig, bx3 = plt.subplots()
bx3.plot(fix_time3_s1, voltage3_s1, 'g', linewidth=2.0)
bx3.plot(fix_time3_s2, voltage3_s2, 'b', linewidth=2.0)
bx3.plot(fix_time3_s3, voltage3_s3, 'm', linewidth=2.0)
bx3.legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})
bx3.set_title('CD - 100e-6 A Comparison')
bx3.set_xlabel('Time (s)')
bx3.set_ylabel('Voltage (V)')

fig.savefig('CD - 100e-6 A Comparions.png', dpi=1000)

# Run 4
fig, bx4 = plt.subplots()
bx4.plot(fix_time4_s1, voltage4_s1, 'g', linewidth=2.0)
bx4.plot(fix_time4_s2, voltage4_s2, 'b', linewidth=2.0)
bx4.plot(fix_time4_s3, voltage4_s3, 'm', linewidth=2.0)
bx4.legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})
bx4.set_title('CD - 200e-6 A Comparison')
bx4.set_xlabel('Time (s)')
bx4.set_ylabel('Voltage (V)')

fig.savefig('CD - 200e-6 A Comparions.png', dpi=1000)

# # Run 5
# fig, bx5 = plt.subplots()
# bx5.plot(fix_time5_s1,voltage5_s1,'g', linewidth=2.0)
# bx5.plot(fix_time5_s2,voltage5_s2,'b', linewidth=2.0)
# bx5.legend(['No Vacuum','24 hr Vacuum'],loc='best')
# bx5.set_title('CD - 500e-6 A Comparison')
# bx5.set_xlabel('Time (s)')
# bx5.set_ylabel('Voltage (V)')

# fig.savefig('CD - 500e-6 A Comparions.png', dpi = 1000)

# Plot all together (4x4)
fig, axs2 = plt.subplots(2, 2, gridspec_kw={'hspace': 0.4})

axs2[0, 0].plot(fix_time1_s1, voltage1_s1, 'g', linewidth=2.0)
axs2[0, 0].plot(fix_time1_s2, voltage1_s2, 'b', linewidth=2.0)
axs2[0, 0].plot(fix_time1_s3, voltage1_s3, 'm', linewidth=2.0)
axs2[0, 0].set_title('(a)')
axs2[0, 0].set_ylabel('Voltage (V)')
axs2[0, 0].legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})

axs2[0, 1].plot(fix_time2_s1, voltage2_s1, 'g', linewidth=2.0)
axs2[0, 1].plot(fix_time2_s2, voltage2_s2, 'b', linewidth=2.0)
axs2[0, 1].plot(fix_time2_s3, voltage2_s3, 'm', linewidth=2.0)
axs2[0, 1].set_title('(b)')
axs2[0, 1].legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})

axs2[1, 0].plot(fix_time3_s1, voltage3_s1, 'g', linewidth=2.0)
axs2[1, 0].plot(fix_time3_s2, voltage3_s2, 'b', linewidth=2.0)
axs2[1, 0].plot(fix_time3_s3, voltage3_s3, 'm', linewidth=2.0)
axs2[1, 0].set_title('(c)')
axs2[1, 0].set_xlabel('Time (s)')
axs2[1, 0].set_ylabel('Voltage (V)')
axs2[1, 0].ticklabel_format(axis='y', style='sci', scilimits=(1, -5))
axs2[1, 0].legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})

axs2[1, 1].plot(fix_time4_s1, voltage4_s1, 'g', linewidth=2.0)
axs2[1, 1].plot(fix_time4_s2, voltage4_s2, 'b', linewidth=2.0)
axs2[1, 1].plot(fix_time4_s3, voltage4_s3, 'm', linewidth=2.0)
axs2[1, 1].set_title('(d)')
axs2[1, 1].set_xlabel('Time (s)')
axs2[1, 1].ticklabel_format(axis='y', style='sci', scilimits=(1, -5))
axs2[1, 1].legend(['Run 1', 'Run 2', 'Run 3'], loc='upper left', prop={'size': 7})

axs2[0, 0].tick_params(axis='both', which='major', labelsize=5)
axs2[0, 1].tick_params(axis='both', which='major', labelsize=5)
axs2[1, 0].tick_params(axis='both', which='major', labelsize=5)
axs2[1, 1].tick_params(axis='both', which='major', labelsize=5)

fig.savefig('CD S033 S034 S035 wired.png', dpi=1000)