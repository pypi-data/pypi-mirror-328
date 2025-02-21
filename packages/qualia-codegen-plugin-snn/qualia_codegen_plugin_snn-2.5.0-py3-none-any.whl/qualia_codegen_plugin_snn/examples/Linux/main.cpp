// Copyright 2021 (c) Pierre-Emmanuel Novac <penovac@unice.fr> Université Côte d'Azur, CNRS, LEAT. All rights reserved.

#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <memory>
#include <sstream>
#include <fstream> 
#include <vector>
#include <cmath>
#include "SpikingNeuralNetwork.h"
#include "metrics.h"

template<int N>
std::vector<std::array<float, N>> readInputsFromFile(const char *filename) {
	// Read training vectors from CSV file
	std::vector<std::array<float, N>> inputs;
	std::ifstream fin(filename);
	std::string linestr;
	while (std::getline(fin, linestr)) {
		std::istringstream linestrs(linestr);
		std::string floatstr;
		std::array<float, N> floats{};
		for (int i = 0; std::getline(linestrs, floatstr, ','); i++) {
			floats.at(i) = std::strtof(floatstr.c_str(), NULL);
		}
		inputs.push_back(floats);
	}
	return inputs;
}

//Compute testing accuracy
template<size_t InputDims, size_t OutputDims>
void evaluate(const std::vector<std::array<float, InputDims>> &inputs, const std::vector<std::array<float, OutputDims>> &targets) {
	static SpikingNeuralNetwork nn{metrics};

	for (size_t i = 0;  i < inputs.size() ; i++){ //&& i < labels.size()-1000; i++) {
#ifdef MODEL_INPUT_TIMESTEP_MODE_DUPLICATE
		nn.evaluate(inputs.at(i), targets.at(i));
#elif defined(MODEL_INPUT_TIMESTEP_MODE_ITERATE)
		nn.evaluate_timesteps(inputs.at(i), targets.at(i));
#else
	#error "Unknown input timestep mode"
#endif
	}

	auto metrics_result = nn.getMetricsResult();

	for (size_t i = 0; i < metrics.size() && i < metrics_result.size(); i++) {
		std::cerr << metrics[i]->name() << "=" << metrics_result[i] << std::endl;
	}
}

int main(int argc, const char *argv[]) {
	if (argc != 3) {
		std::cerr << "Usage: " << argv[0] << " testX.csv testY.csv" << std::endl;
		exit(1);
	}


#ifdef MODEL_INPUT_TIMESTEP_MODE_DUPLICATE
	auto inputs = readInputsFromFile<MODEL_INPUT_DIMS>(argv[1]);
#elif defined(MODEL_INPUT_TIMESTEP_MODE_ITERATE)
	auto inputs = readInputsFromFile<MODEL_INPUT_TIMESTEPS * MODEL_INPUT_DIMS>(argv[1]);
#else
	#error "Unknown input timestep mode"
#endif
	auto labels = readInputsFromFile<MODEL_OUTPUT_SAMPLES>(argv[2]);

	evaluate(inputs, labels);

	return 0;
}
