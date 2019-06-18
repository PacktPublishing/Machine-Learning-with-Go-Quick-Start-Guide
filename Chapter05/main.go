package main

import (
	tf "github.com/tensorflow/tensorflow/tensorflow/go"
	"fmt"
	"log"
)

func makeTensorFromImage(img string) (*tf.Tensor, error) {
	t := make([][]float32, 1)
	t[0] = make([]float32, 784)
	tensor, err := tf.NewTensor(t)
	return tensor, err
}

func main() {
	savedModel, err := tf.LoadSavedModel("./saved_model", []string{"serve"}, nil)
	if err != nil {
		log.Fatalf("failed to load model: %v", err)
	}
	input := savedModel.Graph.Operation("input_input_1")
	output := savedModel.Graph.Operation("output_1/BiasAdd")

	session := savedModel.Session
	graph := savedModel.Graph
	if err != nil {
		log.Fatal(err)
	}
	defer session.Close()
	fmt.Println("Successfully imported model!")
	tensor, err := makeTensorFromImage("")
	if err != nil {
		log.Fatal(err)
	}
	prediction, err := session.Run(
		map[tf.Output]*tf.Tensor{
			graph.Operation(input.Name()).Output(0): tensor,
		},
		[]tf.Output{
			graph.Operation(output.Name()).Output(0),
		},
		nil)
	if err != nil {
		log.Fatal(err)
	}

	probability := prediction[0].Value().([][]float32)[0][0]
	if probability > 0.5 {
		fmt.Printf("It's a pair of trousers! Probability: %v\n", probability)
	} else {
		fmt.Printf("It's NOT a pair of trousers! Probability: %v\n", probability)
	}

}