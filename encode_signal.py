#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Encode Signal
# Generated: Thu Jan 16 13:56:32 2020
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

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class encode_signal(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Encode Signal")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Encode Signal")
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

        self.settings = Qt.QSettings("GNU Radio", "encode_signal")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.inputi = inputi = '/home/afonsonf/sandbox/repos/rcm/rcm-trabalho/input_bin.txt'
        self.baseband_freq = baseband_freq = 676
        self.spacing = spacing = 1
        self.samples_per_symbol = samples_per_symbol = int (samp_rate / baseband_freq)
        self.packet = packet = "".join([l.strip() for l in open(inputi)])
        self.carrier_freq = carrier_freq = 432.867e6

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=samples_per_symbol / 4,
                decimation=1,
                taps=(1, ),
                fractional_bw=4,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	carrier_freq, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(True)



        self.digital_map_bb_0 = digital.map_bb(([0x8, 0xE, 0x0]))
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('/home/afonsonf/sandbox/repos/rcm/rcm-trabalho/signal.wav', 1, 2000000, 8)
        self.blocks_vector_source_x_0 = blocks.vector_source_b([ int (x) for x in packet ] + [ 2 ] * spacing, False, 1, [])
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(4)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1, ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(samples_per_symbol / 4, 1, 4000, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_moving_average_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "encode_signal")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samples_per_symbol(int (self.samp_rate / self.baseband_freq))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(self.carrier_freq, self.samp_rate)

    def get_inputi(self):
        return self.inputi

    def set_inputi(self, inputi):
        self.inputi = inputi
        self.set_packet("".join([l.strip() for l in open(self.inputi)]))

    def get_baseband_freq(self):
        return self.baseband_freq

    def set_baseband_freq(self, baseband_freq):
        self.baseband_freq = baseband_freq
        self.set_samples_per_symbol(int (self.samp_rate / self.baseband_freq))

    def get_spacing(self):
        return self.spacing

    def set_spacing(self, spacing):
        self.spacing = spacing
        self.blocks_vector_source_x_0.set_data([ int (x) for x in self.packet ] + [ 2 ] * self.spacing, [])

    def get_samples_per_symbol(self):
        return self.samples_per_symbol

    def set_samples_per_symbol(self, samples_per_symbol):
        self.samples_per_symbol = samples_per_symbol
        self.blocks_moving_average_xx_0.set_length_and_scale(self.samples_per_symbol / 4, 1)

    def get_packet(self):
        return self.packet

    def set_packet(self, packet):
        self.packet = packet
        self.blocks_vector_source_x_0.set_data([ int (x) for x in self.packet ] + [ 2 ] * self.spacing, [])

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.qtgui_sink_x_0.set_frequency_range(self.carrier_freq, self.samp_rate)


def main(top_block_cls=encode_signal, options=None):

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
