#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Decode
# Generated: Thu Jan 16 14:13:42 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sys
from gnuradio import qtgui


class decode_(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Decode ")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Decode ")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "decode_")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.baseband_freq = baseband_freq = 676
        self.samples_per_symbol = samples_per_symbol = int (samp_rate / baseband_freq)
        self.carrier_freq = carrier_freq = 432.867e6

        ##################################################
        # Blocks
        ##################################################
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_ff(digital.TED_SIGNAL_TIMES_SLOPE_ML, samples_per_symbol/4, 0.045, 1.0, 1.0, 1.5, 1, digital.constellation_bpsk().base(), digital.IR_PFB_NO_MF, 128, ([]))
        self.digital_map_bb_0_1 = digital.map_bb(([10, 0, 0, 0, 0, 0, 0, 0, 48, 0, 0, 0, 0, 0, 49, 0]))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/afonsonf/sandbox/repos/rcm/rcm-trabalho/signal.wav', False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(4)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/afonsonf/sandbox/repos/rcm/rcm-trabalho/out_bin.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_map_bb_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_map_bb_0_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.blocks_float_to_uchar_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "decode_")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samples_per_symbol(int (self.samp_rate / self.baseband_freq))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_baseband_freq(self):
        return self.baseband_freq

    def set_baseband_freq(self, baseband_freq):
        self.baseband_freq = baseband_freq
        self.set_samples_per_symbol(int (self.samp_rate / self.baseband_freq))

    def get_samples_per_symbol(self):
        return self.samples_per_symbol

    def set_samples_per_symbol(self, samples_per_symbol):
        self.samples_per_symbol = samples_per_symbol

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq


def main(top_block_cls=decode_, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
