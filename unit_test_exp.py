# !/usr/bin/env python
# coding=utf8


from unittest import TestCase, mock, main

import mock_exp as client


class TestStringMethods(TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        client.send_request = success_send
        self.assertEqual(client.get_result(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        client.send_request = fail_send
        self.assertEqual(client.get_result(), '404')

    # 这次我们要检查get_result()函数调用send_request()函数时，传递的参数类型是否正确。我们可以像下面这样使用mock对象
    def test_call_send_request_with_right_arguments(self):
        client.send_request = mock.Mock()
        client.get_result()
        self.assertEqual(client.send_request.called, True)
        call_args = client.send_request.call_args
        self.assertIsInstance(call_args[0][0], str)

    # 用path限制作用域
    def test_success_requestV2(self):
        status_code = '200'
        success_send = mock.Mock(return_value=status_code)
        with mock.patch('mock_exp.send_request', success_send):
            from mock_exp import get_result
            self.assertEqual(get_result(), status_code)

    # 用path限制作用域
    def test_fail_requestV2(self):
        status_code = '404'
        fail_send = mock.Mock(return_value=status_code)
        with mock.patch('mock_exp.send_request', fail_send):
            from mock_exp import get_result
            self.assertEqual(get_result(), status_code)

    # path object和patch的用法差不多
    def test_fail_requestV3(self):
        status_code = '404'
        fail_send = mock.Mock(return_value=status_code)
        with mock.patch.object(client, 'send_request', fail_send):
            from mock_exp import get_result
            self.assertEqual(get_result(), status_code)


if __name__ == '__main__':
    main()
