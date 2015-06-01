# -*- coding: utf-8 -*- 
from math import sin, pi
import sys


class Synthesizer(object):
	#função responsavel por produzir uma sequencia de amostras
	#que iram representar a forma de onda de cada nota
	def synthesize(self, organ_registry_string, interpreter_list):
		organ_reg_int = []
		for i in range(0, len(organ_registry_string)):
			tmp = list(organ_registry_string)
			organ_reg_int.append(int(tmp[i]))

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
			output_samples.append(get_samples(organ_reg_int, duration[i], frequencies[i]))

		#normalizar as samples antes de dar append para o output final

		normalized_output_samples = normalize(output_samples)

		#append dos valores para a lista de dicionarios a ser devolvida
		for i in range(0, len(interpreter_list)):
			output.append({'freq': frequencies[i], 'samples': normalized_output_samples[i]})

		return output 

	#funcao responsavel por produzir as samples de uma nota
	#tendo em conta a amplitude, duracao e frequencia
	#devolve uma lista com as samples de uma nota
	def get_samples(self, org_reg_list, duration, frequency):
		rate = 44100
		data = []
		mult_frequencies = get_mult_freq(frequency)

		for i in range(0, int(rate*duration)):
			data.append(
				(org_reg_list[0]/8 * sin(2*pi*mult_frequencies[0]*i/rate)) +
				(org_reg_list[1]/8 * sin(2*pi*mult_frequencies[1]*i/rate)) +
				(org_reg_list[2]/8 * sin(2*pi*mult_frequencies[2]*i/rate)) +
				(org_reg_list[3]/8 * sin(2*pi*mult_frequencies[3]*i/rate)) +
				(org_reg_list[4]/8 * sin(2*pi*mult_frequencies[4]*i/rate)) +
				(org_reg_list[5]/8 * sin(2*pi*mult_frequencies[5]*i/rate)) +
				(org_reg_list[6]/8 * sin(2*pi*mult_frequencies[6]*i/rate)) +
				(org_reg_list[7]/8 * sin(2*pi*mult_frequencies[7]*i/rate)) +
				(org_reg_list[8]/8 * sin(2*pi*mult_frequencies[8]*i/rate))
			)
		return data

	def get_mult_freq(self, freq):
		values = [1/2.0, 2/3.0 , 1, 2, 3, 4, 5, 6, 8]
		data = []
		for i in range(0, 9):
			data.append(freq*values[i])
		data = map(int, data)
		return data 

	#funcao responsavel pela normalizacao das samples
	def normalize(self, data):
		MAX_VALUE = 2 ** 15 - 1  #32767
		maximum = 0
		for k in data:
			for v in k:
				if abs(v) > maximum:
					maximum = abs(v) 

		if not maximum == 0:
			normalize_factor = (float(MAX_VALUE)/ maximum)

		normalized_data = []
		tmp = []
		for i in data:
			tmp = []
			for values in i:
				tmp.append(values * normalize_factor)
			normalized_data.append(tmp)
		return normalized_data