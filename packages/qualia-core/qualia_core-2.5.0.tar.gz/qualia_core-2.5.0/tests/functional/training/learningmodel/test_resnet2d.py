from unittest import TestCase

class TestModelsResNet2D(TestCase):
    def setUp(self):
        import numpy as np
        from qualia_core.datamodel import RawDataModel
        from qualia_core.datamodel.RawDataModel import RawData, RawDataSets
        train = RawData(np.ones((2, 64, 64, 1), dtype=np.float32), np.array([[1, 0], [1, 0]]))
        test = RawData(np.ones((2, 64, 64, 1), dtype=np.float32), np.array([[1, 0], [0, 1]]))
        self.__data = RawDataModel(sets=RawDataSets(train=train, test=test), name='test_resnet2d')
        self.__model_params = {
            'filters': (4, 6),
            'kernel_sizes': (5, 5),

            'num_blocks': (2,),
            'strides': (1, 2),
            'paddings': (2, 2),

            'prepool': 2,
            'batch_norm': True,
            'bn_momentum': 0.95,

            'dims': 2
            }

    def test_resnet_2d_keras(self):
        from qualia_core import qualia
        from qualia_core.learningframework import Keras
        from qualia_core.learningmodel.keras import ResNet
        from tensorflow.keras.layers import InputLayer, Dense, Activation, Flatten, ZeroPadding2D, Conv2D, AveragePooling2D, MaxPooling2D, BatchNormalization, Dropout, Add
        from tensorflow.keras.activations import relu, softmax

        model = ResNet

        framework = Keras()

        trainresult = qualia.train(self.__data,
                        train_epochs=1,
                        iteration=1,
                        model_name='test_resnet_2d_keras',
                        model=model,
                        model_params=self.__model_params,
                        optimizer={'kind': 'Adam'},
                        framework=framework,
                        )
        self.assertEqual(trainresult.name, 'test_resnet_2d_keras')
        self.assertEqual(trainresult.i, 1)
        self.assertEqual(trainresult.model.input_shape, (None, 64, 64, 1))
        self.assertEqual(trainresult.model.output_shape, (None, 2))

        self.assertEqual(len(trainresult.model.layers), 32)

        self.assertIsInstance(trainresult.model.get_layer('input_layer'), InputLayer)
        # prepool
        self.assertIsInstance(trainresult.model.get_layer('average_pooling2d'), AveragePooling2D)
        self.assertEqual(tuple(trainresult.model.get_layer('average_pooling2d').pool_size), (2, 2))
        self.assertEqual(tuple(trainresult.model.get_layer('average_pooling2d').strides), (2, 2))

        # preconv
        self.assertIsInstance(trainresult.model.get_layer('zero_padding2d'), ZeroPadding2D)
        self.assertEqual(tuple(trainresult.model.get_layer('zero_padding2d').padding), ((2, 2), (2, 2)))
        self.assertIsInstance(trainresult.model.get_layer('conv2d'), Conv2D)
        self.assertEqual(tuple(trainresult.model.get_layer('conv2d').kernel.shape), (5, 5, 1, 4)) # 5*5*1*4 = 100
        self.assertEqual(trainresult.model.get_layer('conv2d').bias, None)
        self.assertIsInstance(trainresult.model.get_layer('batch_normalization'), BatchNormalization)
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization').moving_mean.shape), (4,)) # 4
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization').moving_variance.shape), (4, )) # 4
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization').gamma.shape), (4, )) # 4
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization').beta.shape), (4, )) # 4
        self.assertIsInstance(trainresult.model.get_layer('activation'), Activation)
        self.assertEqual(trainresult.model.get_layer('activation').activation, relu)

        # 1st res block
        # 1st conv
        self.assertIsInstance(trainresult.model.get_layer('zero_padding2d_1'), ZeroPadding2D)
        self.assertEqual(tuple(trainresult.model.get_layer('zero_padding2d_1').padding), ((2, 2), (2, 2)))
        self.assertIsInstance(trainresult.model.get_layer('conv2d_1'), Conv2D)
        self.assertEqual(tuple(trainresult.model.get_layer('conv2d_1').kernel.shape), (5, 5, 4, 6)) # 5*4*6 = 600
        self.assertEqual(trainresult.model.get_layer('conv2d_1').bias, None)
        self.assertIsInstance(trainresult.model.get_layer('batch_normalization_1'), BatchNormalization)
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_1').moving_mean.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_1').moving_variance.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_1').gamma.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_1').beta.shape), (6, )) # 6
        self.assertIsInstance(trainresult.model.get_layer('max_pooling2d'), MaxPooling2D)
        self.assertEqual(tuple(trainresult.model.get_layer('max_pooling2d').pool_size), (2, 2))
        self.assertEqual(tuple(trainresult.model.get_layer('max_pooling2d').strides), (2, 2))
        self.assertIsInstance(trainresult.model.get_layer('activation_1'), Activation)
        self.assertEqual(trainresult.model.get_layer('activation_1').activation, relu)
        # 2nd conv
        self.assertIsInstance(trainresult.model.get_layer('conv_ref'), Conv2D)
        self.assertEqual(tuple(trainresult.model.get_layer('conv_ref').kernel.shape), (5, 5, 6, 6)) # 5*6*6 = 900
        self.assertEqual(trainresult.model.get_layer('conv_ref').bias, None)
        self.assertIsInstance(trainresult.model.get_layer('batch_normalization_2'), BatchNormalization)
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_2').moving_mean.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_2').moving_variance.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_2').gamma.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_2').beta.shape), (6, )) # 6
        # shortcut
        self.assertIsInstance(trainresult.model.get_layer('zero_padding2d_2'), ZeroPadding2D)
        self.assertEqual(tuple(trainresult.model.get_layer('zero_padding2d_2').padding), ((2, 2), (2, 2)))
        self.assertIsInstance(trainresult.model.get_layer('conv_shortcut'), Conv2D)
        self.assertEqual(tuple(trainresult.model.get_layer('conv_shortcut').kernel.shape), (1, 1, 4, 6)) # 1*1*4*6 = 24
        self.assertEqual(trainresult.model.get_layer('conv_shortcut').bias, None)
        self.assertIsInstance(trainresult.model.get_layer('batch_normalization_3'), BatchNormalization)
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_3').moving_mean.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_3').moving_variance.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_3').gamma.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_3').beta.shape), (6, )) # 6
        self.assertIsInstance(trainresult.model.get_layer('max_pooling2d_1'), MaxPooling2D)
        self.assertEqual(tuple(trainresult.model.get_layer('max_pooling2d_1').pool_size), (2, 2))
        self.assertEqual(tuple(trainresult.model.get_layer('max_pooling2d_1').strides), (2, 2))
        # add
        self.assertIsInstance(trainresult.model.get_layer('add'), Add)
        self.assertIsInstance(trainresult.model.get_layer('activation_2'), Activation)
        self.assertEqual(trainresult.model.get_layer('activation_2').activation, relu)


        # 2nd conv block
        # 1st conv
        self.assertIsInstance(trainresult.model.get_layer('zero_padding2d_3'), ZeroPadding2D)
        self.assertEqual(tuple(trainresult.model.get_layer('zero_padding2d_3').padding), ((2, 2), (2, 2)))
        self.assertIsInstance(trainresult.model.get_layer('conv2d_2'), Conv2D)
        self.assertEqual(tuple(trainresult.model.get_layer('conv2d_2').kernel.shape), (5, 5, 6, 6)) # 5*6*6 = 900
        self.assertEqual(trainresult.model.get_layer('conv2d_2').bias, None)
        self.assertIsInstance(trainresult.model.get_layer('batch_normalization_4'), BatchNormalization)
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_4').moving_mean.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_4').moving_variance.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_4').gamma.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_4').beta.shape), (6, )) # 6
        self.assertIsInstance(trainresult.model.get_layer('activation_3'), Activation)
        self.assertEqual(trainresult.model.get_layer('activation_3').activation, relu)
        # 2nd conv
        self.assertIsInstance(trainresult.model.get_layer('conv_ref_1'), Conv2D)
        self.assertEqual(tuple(trainresult.model.get_layer('conv_ref_1').kernel.shape), (5, 5, 6, 6)) # 5*6*6 = 900
        self.assertEqual(trainresult.model.get_layer('conv_ref_1').bias, None)
        self.assertIsInstance(trainresult.model.get_layer('batch_normalization_5'), BatchNormalization)
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_5').moving_mean.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_5').moving_variance.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_5').gamma.shape), (6, )) # 6
        self.assertEqual(tuple(trainresult.model.get_layer('batch_normalization_5').beta.shape), (6, )) # 6
        # shortcut
        self.assertIsInstance(trainresult.model.get_layer('zero_padding2d_4'), ZeroPadding2D)
        self.assertEqual(tuple(trainresult.model.get_layer('zero_padding2d_4').padding), ((2, 2), (2, 2)))
        # add
        self.assertIsInstance(trainresult.model.get_layer('add_1'), Add)
        self.assertIsInstance(trainresult.model.get_layer('activation_4'), Activation)
        self.assertEqual(trainresult.model.get_layer('activation_4').activation, relu)

        self.assertIsInstance(trainresult.model.get_layer('max_pooling2d_2'), MaxPooling2D)
        self.assertEqual(tuple(trainresult.model.get_layer('max_pooling2d_2').pool_size), (16, 16))
        self.assertEqual(tuple(trainresult.model.get_layer('max_pooling2d_2').strides), (16, 16))

        self.assertIsInstance(trainresult.model.get_layer('flatten'), Flatten)

        # fc
        self.assertIsInstance(trainresult.model.get_layer('dense'), Dense)
        self.assertEqual(trainresult.model.get_layer('dense').kernel.shape, (6, 2)) # 6*2 = 12
        self.assertEqual(trainresult.model.get_layer('dense').bias.shape, (2, )) # 2

        # softmax
        self.assertIsInstance(trainresult.model.get_layer('activation_5'), Activation)
        self.assertEqual(trainresult.model.get_layer('activation_5').activation, softmax)

        # first layer 10 weights/10 biases, second layer 10*10 weights (10 inputs, 10 outputs)/10 biases, 3rd layer 10*2 weights (10 inputs 2 outputs)/2 biases, 4 bytes (float32)
        self.assertEqual(trainresult.mem_params, (5*5*1*4 + 4*4 + 5*5*4*6 + 6*4 + 5*5*6*6 + 6*4 + 1*1*4*6 + 6*4 + 5*5*6*6 + 6*4 + 5*5*6*6 + 6*4 + 6*2 + 2) * 4)
        self.assertEqual(trainresult.acc, 0.5) # Same data in one or the other class, should have 50% acc
        self.assertEqual(trainresult.framework, framework)

    def test_resnet_2d_pytorch(self):
        from qualia_core import qualia
        from qualia_core.learningframework import PyTorch
        from qualia_core.learningmodel.pytorch import ResNet
        from qualia_core.learningmodel.pytorch.layers import Add
        from torch.nn import Flatten, Linear, ReLU, AvgPool2d, MaxPool2d, Conv2d, BatchNorm2d, Dropout

        model = ResNet

        framework = PyTorch(enable_progress_bar=False)

        trainresult = qualia.train(self.__data,
                        train_epochs=1,
                        iteration=1,
                        model_name='test_resnet_2d_pytorch',
                        model=model,
                        model_params=self.__model_params,
                        optimizer={'kind': 'Adam'},
                        framework=framework,
                        )
        self.assertEqual(trainresult.name, 'test_resnet_2d_pytorch')
        self.assertEqual(trainresult.i, 1)
        #self.assertEqual(trainresult.model.input_shape, (None, 1, 1)) # Not supported in PyTorch
        #self.assertEqual(trainresult.model.output_shape, (None, 2)), Not supported in PyTorch

        self.assertEqual(len(list(trainresult.model.children())), 8)
        self.assertEqual(len(list(trainresult.model.layers.children())), 1)
        self.assertEqual(len(list(trainresult.model.layers[0].children())), 2)
        self.assertEqual(len(list(trainresult.model.layers[0][0].children())), 11)
        self.assertEqual(len(list(trainresult.model.layers[0][1].children())), 7)

        # prepool
        self.assertIsInstance(trainresult.model.prepool, AvgPool2d)
        self.assertEqual(trainresult.model.prepool.kernel_size, 2)
        self.assertEqual(trainresult.model.prepool.stride, 2)

        # preconv
        self.assertIsInstance(trainresult.model.conv1, Conv2d)
        self.assertEqual(tuple(trainresult.model.conv1.padding), (2, 2))
        self.assertEqual(tuple(trainresult.model.conv1.weight.shape), (4, 1, 5, 5)) # 4*1*5*5 = 100
        self.assertEqual(trainresult.model.conv1.bias, None)
        self.assertIsInstance(trainresult.model.bn1, BatchNorm2d)
        self.assertEqual(tuple(trainresult.model.bn1.weight.shape), (4,)) # 4
        self.assertEqual(tuple(trainresult.model.bn1.bias.shape), (4, )) # 4
        self.assertIsInstance(trainresult.model.relu1, ReLU)

        # 1st res block
        # 1st conv
        self.assertIsInstance(trainresult.model.layers[0][0].conv1, Conv2d)
        self.assertEqual(tuple(trainresult.model.layers[0][0].conv1.padding), (2, 2))
        self.assertEqual(tuple(trainresult.model.layers[0][0].conv1.weight.shape), (6, 4, 5, 5)) # 6*4*5*5 = 600
        self.assertEqual(trainresult.model.layers[0][0].conv1.bias, None)
        self.assertIsInstance(trainresult.model.layers[0][0].bn1, BatchNorm2d)
        self.assertEqual(tuple(trainresult.model.layers[0][0].bn1.weight.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.layers[0][0].bn1.bias.shape), (6, )) # 6
        self.assertIsInstance(trainresult.model.layers[0][0].pool1, MaxPool2d)
        self.assertEqual(trainresult.model.layers[0][0].pool1.kernel_size, 2)
        self.assertEqual(trainresult.model.layers[0][0].pool1.stride, 2)
        self.assertIsInstance(trainresult.model.layers[0][0].relu1, ReLU)
        # 2nd conv
        self.assertIsInstance(trainresult.model.layers[0][0].conv2, Conv2d)
        self.assertEqual(tuple(trainresult.model.layers[0][0].conv2.padding), (2, 2))
        self.assertEqual(tuple(trainresult.model.layers[0][0].conv2.weight.shape), (6, 6, 5, 5)) # 6*6*5 = 900
        self.assertEqual(trainresult.model.layers[0][0].conv2.bias, None)
        self.assertIsInstance(trainresult.model.layers[0][0].bn2, BatchNorm2d)
        self.assertEqual(tuple(trainresult.model.layers[0][0].bn2.weight.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.layers[0][0].bn2.bias.shape), (6, )) # 6
        # shortcut
        self.assertIsInstance(trainresult.model.layers[0][0].sconv, Conv2d)
        self.assertEqual(tuple(trainresult.model.layers[0][0].sconv.padding), (0, 0))
        self.assertEqual(tuple(trainresult.model.layers[0][0].sconv.weight.shape), (6, 4, 1, 1)) # 6*4*1*1 = 24
        self.assertEqual(trainresult.model.layers[0][0].sconv.bias, None)
        self.assertIsInstance(trainresult.model.layers[0][0].sbn, BatchNorm2d)
        self.assertEqual(tuple(trainresult.model.layers[0][0].sbn.weight.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.layers[0][0].sbn.bias.shape), (6, )) # 6
        self.assertIsInstance(trainresult.model.layers[0][0].spool, MaxPool2d)
        self.assertEqual(trainresult.model.layers[0][0].spool.kernel_size, 2)
        self.assertEqual(trainresult.model.layers[0][0].spool.stride, 2)
        # add
        self.assertIsInstance(trainresult.model.layers[0][0].add, Add)
        self.assertIsInstance(trainresult.model.layers[0][0].relu, ReLU)


        # 2nd conv block
        # 1st conv
        self.assertIsInstance(trainresult.model.layers[0][1].conv1, Conv2d)
        self.assertEqual(tuple(trainresult.model.layers[0][1].conv1.padding), (2, 2))
        self.assertEqual(tuple(trainresult.model.layers[0][1].conv1.weight.shape), (6, 6, 5, 5)) # 6*6*5*5 = 900
        self.assertEqual(trainresult.model.layers[0][1].conv1.bias, None)
        self.assertIsInstance(trainresult.model.layers[0][1].bn1, BatchNorm2d)
        self.assertEqual(tuple(trainresult.model.layers[0][1].bn1.weight.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.layers[0][1].bn1.bias.shape), (6, )) # 6
        self.assertIsInstance(trainresult.model.layers[0][1].relu1, ReLU)
        # 2nd conv
        self.assertIsInstance(trainresult.model.layers[0][1].conv2, Conv2d)
        self.assertEqual(tuple(trainresult.model.layers[0][1].conv2.padding), (2, 2))
        self.assertEqual(tuple(trainresult.model.layers[0][1].conv2.weight.shape), (6, 6, 5, 5)) # 6*6*5*5 = 900
        self.assertEqual(trainresult.model.layers[0][1].conv2.bias, None)
        self.assertIsInstance(trainresult.model.layers[0][1].bn2, BatchNorm2d)
        self.assertEqual(tuple(trainresult.model.layers[0][1].bn2.weight.shape), (6,)) # 6
        self.assertEqual(tuple(trainresult.model.layers[0][1].bn2.bias.shape), (6, )) # 6
        # add
        self.assertIsInstance(trainresult.model.layers[0][1].add, Add)
        self.assertIsInstance(trainresult.model.layers[0][1].relu, ReLU)

        self.assertIsInstance(trainresult.model.postpool, MaxPool2d)
        self.assertEqual(tuple(trainresult.model.postpool.kernel_size), (16, 16))
        self.assertEqual(tuple(trainresult.model.postpool.stride), (16, 16))

        self.assertIsInstance(trainresult.model.flatten, Flatten)

        # fc
        self.assertIsInstance(trainresult.model.linear, Linear)
        self.assertEqual(trainresult.model.linear.weight.shape, (2, 6)) # 2*6 = 12
        self.assertEqual(trainresult.model.linear.bias.shape, (2, )) # 2


        self.assertEqual(trainresult.mem_params, (5*5*1*4 + 4*2 + 5*5*4*6 + 6*2 + 5*5*6*6 + 6*2 + 1*1*4*6 + 6*2 + 5*5*6*6 + 6*2 + 5*5*6*6 + 6*2 + 6*2 + 2) * 4)
        self.assertEqual(trainresult.acc, 0.5) # Same data in one or the other class, should have 50% acc
        self.assertEqual(trainresult.framework, framework)
