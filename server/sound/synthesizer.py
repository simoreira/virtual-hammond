# -*- coding: utf-8 -*- 
from math import sin, pi
from struct import pack #apagar
import sys
import wave

#função responsavel por produzir uma sequencia de amostras
#que iram representar a forma de onda de cada nota
def synthesize(organ_registry_string, interpreter_list):
	o_r_int_list = []
	for i in range(0, len(organ_registry_string)):
		tmp = list(organ_registry_string)
		o_r_int_list.append(int(tmp[i]))

	duration = []
	frequencies = []
	output_samples = []
	output = []
	#parse dos pares recebidos pelo interpretador 
	#para duas listas, uma com as durações e outra
	#com as frequencias
	for i in range(0, len(interpreter_list)):
		duration.append(interpreter_list[i][0])
		frequencies.append(interpreter_list[i][1])

	#criação da lista que será devolvida por este modulo
	#lista esta composta por um numero de dicionarios 
	#equivalente ao numero de notas
	#output samples é uma lista que contem listas de samples
	for i in range(0, len(interpreter_list)):
		output_samples.append(get_samples(o_r_int_list, duration[i], frequencies[i]))

	#append dos valores para a lista de dicionarios a ser devolvida
	for i in range(0, len(interpreter_list)):
		output.append({'freq': frequencies[i], 'samples': output_samples[i]})

	return output 

#funcao responsavel por produzir as samples de uma nota
#tendo em conta a amplitude, duracao e frequencia
#devolve uma lista com as samples de uma nota
def get_samples(amp_list, duration, frequency):
	rate = 44100
	data = []
	mult_frequencies = get_mult_freq(frequency)

	for i in range(0, int(rate*duration)):
		data.append(
			(amp_list[0] * sin(2*pi*mult_frequencies[0]*i/rate)) +
			(amp_list[1] * sin(2*pi*mult_frequencies[1]*i/rate)) +
			(amp_list[2] * sin(2*pi*mult_frequencies[2]*i/rate)) +
			(amp_list[3] * sin(2*pi*mult_frequencies[3]*i/rate)) +
			(amp_list[4] * sin(2*pi*mult_frequencies[4]*i/rate)) +
			(amp_list[5] * sin(2*pi*mult_frequencies[5]*i/rate)) +
			(amp_list[6] * sin(2*pi*mult_frequencies[6]*i/rate)) +
			(amp_list[7] * sin(2*pi*mult_frequencies[7]*i/rate)) +
			(amp_list[8] * sin(2*pi*mult_frequencies[8]*i/rate))
		)
	normalize(data)
	return data

def get_mult_freq(freq):
	values = [1/2.0, 2/3.0 , 1, 2, 3, 4, 5, 6, 8]
	data = []
	for i in range(0, 9):
		data.append(freq*values[i])
	data = map(int, data)
	return data 

#funcao responsavel pela normalizacao das samples
def normalize(data):
	MAX_VALUE = 2 ** 15 - 1  #32767
	maximum = max(abs(i) for i in data)
	normalize_factor = 1
	if not maximum == 0:
		normalize_factor = (float(MAX_VALUE)/ maximum)

	data_to_return = []
	for i in data:
		data_to_return.append(i * normalize_factor)
	return data_to_return
#
#------------------------------APAGAR------------------------------------
def main(argv):
	wv = wave.open(argv[1], 'w')
	wv.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

	data = []
	teste1 = [
	(0.5625, 1046),
	(0.3750, 1318),
	(0.3750, 1479),
	(0.1875, 1760),
	(0.5625, 1567),
	(0.3750, 1318),
	(0.3750, 1046),
	(0.1875, 880),
	(0.1875, 739),
	(0.1875, 739),
	(0.1875, 739),
	(0.7500, 783),
	(0.1875, 0),
	(0.1875, 0),
	(0.1875, 523),
	(0.1875, 523),
	(0.1875, 739),
	(0.1875, 739),
	(0.1875, 739),
	(0.1875, 783),
	(0.5625, 932),
	(0.1875, 1046),
	(0.1875, 1046),
	(0.1875, 1046),
	(0.3750, 1046)
	]
	
	data = synthesize("888888888", teste1)
	wvData = ''
	for v in range(0, len(data)):
		for i in range(0, len(data[v]['samples'])):
			wvData += pack('h', data[v]['samples'][i])

	wv.writeframes(wvData)
	wv.close()
main(sys.argv)