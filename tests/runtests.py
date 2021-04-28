#!/usr/bin/env python2.7
# Copyright 2016-2021 XMOS LIMITED.
# This Software is subject to the terms of the XMOS Public Licence: Version 1.
import xmostest, sys, subprocess

if __name__ == "__main__":
    xmostest.init()
    xmostest.register_group("lib_src", "asrc_test", "Test ASRC conversion across sample rates",
                            "This test iterates through all input and output sample rates using input 1KHz sine at 0db and 10/11KHz intermodulation tones. It checks the output against golden results generated by the original ASRC deliverable from Digimath.")
    xmostest.register_group("lib_src", "ssrc_test", "Test SSRC conversion across sample rates",
                            "This test iterates through all input and output sample rates using input 1KHz sine at 0db and 10/11KHz intermodulation tones. It checks the output against golden results generated by the original SSRC deliverable from Digimath.")
    xmostest.register_group("lib_src", "fixed_factor_of_3_tests", "Test fixed factor of 3 conversion functions.",
                            "These tests check the DS3 and OS3 functions.")

    xmostest.runtests()
    xmostest.finish()
