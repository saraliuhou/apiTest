# -*- coding: utf-8 -*-
import unittest
from hamcrest import *           # 断言库
import cof.rand as CoRandM       # 随机数
import cof.restful as CoRestful  # restful 接口返回值处理
import api_call.distribute.v02.rides as rides # 封装好的接口调用
import api_call.distribute.v02.carpool as carpool
import random
import requests
import datetime

class rideTest(unittest.TestCase):

    def setUp(self):
        """
        测试类的构造方法
        该方法会在每个case运行前被调用一次
        """
        # 实例化接口调用对象
        self.rides = rides.Rides()

        self.carpool = carpool.Carpool()
        # 随机数对象
        self.rnd = CoRandM.CoRand()
        self.rf = CoRestful.Restful()
        self.nowTime = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        # 记录创建资源的标志
        self.flag = 0
        response_createOrder = self.rides.postPassengerOrder("88881713123", 4, 16, self.nowTime)
        message = "创建订单失败"
        code = 201
        data_dict = self.rf.parse_response(response_createOrder, code, message)
        self.ret_id = data_dict['id']
        self.set_create_flag()

    def set_create_flag(self):
        """
        将资源创建标志设置为1，表示有创建过资源
        """
        self.flag = 1
        print("创建资源 %s 成功" % str(self.ret_id))

    def tearDown(self):
        """
        测试类的析构方法
        该方法会在每个case运行后被调用一次
        """
        # 删除服务，回收数据
        if self.flag != 0:
            response_del = self.rides.deleteRide(self.ret_id)
            message = "删除订单失败"
            code = 204
            data_dec_del = self.rf.parse_response(response_del, code, message)
            self.flag = 0
            print("删除资源 %s 成功" % str(self.ret_id))

    def test_fromPendingToRate_ok(self):

        driverPhone = "88889876123"
        driverID = 185
        routeID = 16
        driverInlineResponse = self.carpool.makeDriverOnline(driverPhone, routeID)
        message = "司机出车失败"
        code = 201
        response_dict = self.rf.parse_response(driverInlineResponse, code, message)

        # call api


        acceptResponse = self.rides.rideAccept(driverID, self.ret_id)
        message1 = "司机接单失败"
        code1 = 200
        response_dict = self.rf.parse_response(acceptResponse, code1, message1)

        # 数据完整性断言
        assert_that(response_dict, has_key('id'))
        assert_that(response_dict, has_key('route_id'))
        assert_that(response_dict, has_key('status'))
        assert_that(response_dict, has_key('passengers'))
        assert_that(response_dict, has_key('fee'))
        assert_that(response_dict, has_key('route_direction'))

        # 数据正确性断言
        assert_that(response_dict['id'], equal_to(self.ret_id))
        assert_that(response_dict['route_id'], equal_to(routeID))
        assert_that(response_dict['status'], equal_to("accepted"))

        # arriveResponse = self.rides.rideArrive(self.ret_id)
        #
        # message2 = "到达乘客上车地点状态改变失败"
        # code2 = 200
        #
        # response_dict = self.rf.parse_response(arriveResponse, code2, message2)

        # 数据断言

        progressResponse = self.rides.rideInProgress(self.ret_id)
        message3 = "送驾中状态改变失败"
        code3 = 200

        response_dict = self.rf.parse_response(progressResponse, code3, message3)

        # 数据断言

        # completeResponse = self.rides.rideComplete(self.ret_id)
        # message4 = "订单完成状态改变失败"
        # code4 = 200

        # response_dict = self.rf.parse_response(completeResponse, code4, message4)

        # 数据断言

        # paidResponse = self.rides.ridePay(self.ret_id)
        # message5 = "支付失败"
        # code5 = 201
        #
        # response_dict = self.rf.parse_response(paidResponse, code5, message5)

        # 数据断言
        rateResponse = self.rides.rideRate(self.ret_id, 2)
        message6 = "评价失败"
        code6 = 200

        response_dict = self.rf.parse_response(rateResponse, code6, message6)

        # 数据断言





    def test_reassign_ok(self):
        driverPhone = "88889876123"
        driverID = 185
        routeID = 16
        driverInlineResponse = self.carpool.makeDriverOnline(driverPhone, routeID)
        message = "司机出车失败"
        code = 201
        response_dict = self.rf.parse_response(driverInlineResponse, code, message)

        # call api


        acceptResponse = self.rides.rideAccept(driverID, self.ret_id)
        message1 = "司机接单失败"
        code1 = 200
        response_dict = self.rf.parse_response(acceptResponse, code1, message1)


        ReassignResponse = self.rides.rideReassign(self.ret_id, 2)
        message = "改派失败"
        code = 200
        response_dict = self.rf.parse_response(ReassignResponse, code, message)



        # 正确定断言

    def test_cancelbyPassenger_ok(self):
        CancelResponse = self.rides.rideCancelByPassenger(self.ret_id, 3)
        message = "乘客取消订单失败"
        code = 200
        response_dict = self.rf.parse_response(CancelResponse, code, message)

    def test_cancelByDriver_ok(self):
        driverPhone = "88889876123"
        driverID = 185
        routeID = 16
        driverInlineResponse = self.carpool.makeDriverOnline(driverPhone, routeID)
        message = "司机出车失败"
        code = 201
        response_dict = self.rf.parse_response(driverInlineResponse, code, message)

        # call api


        acceptResponse = self.rides.rideAccept(driverID, self.ret_id)
        message1 = "司机接单失败"
        code1 = 200
        response_dict = self.rf.parse_response(acceptResponse, code1, message1)


        CancelResponse = self.rides.rideCancelByDriver(self.ret_id, 3)
        message = "司机取消失败"
        code = 200
        response_dict = self.rf.parse_response(CancelResponse, code, message)


    def test_expire_ok(self):
        ExpireResponse = self.rides.rideExpire(self.ret_id)
        message = "订单过期失败"
        code = 200
        response_dict = self.rf.parse_response(ExpireResponse, code, message)

    def test_getAllPassengerRidesbyID_ok(self):
        getPassengerRides = self.rides.getPassengerRidesByUserID(187)
        message = "获取乘客订单失败"
        code = 200
        response_dict = self.rf.parse_response(getPassengerRides, code, message)

    def test_getAllDriverRidesbyID_ok(self):
        getdriverRides = self.rides.getDriverOrder(187)
        message = "获取司机订单失败"
        code = 200
        response_dict = self.rf.parse_response(getdriverRides, code, message)

    def test_getAllRides_ok(self):
        getAllRides = self.rides.getAllRides(1, 30)
        message = "获取司机订单失败"
        code = 200
        response_dict = self.rf.parse_response(getAllRides, code, message)

    def test_modifiedRide_ok(self):
        modifiedResponse = self.rides.rideModified(self.ret_id, 999, 5, 88889876123)
        message = "订单修改失败"
        code = 200
        response_dict = self.rf.parse_response(modifiedResponse, code, message)

        # 断言数据完整性
        assert_that(response_dict, has_key('id'))
        assert_that(response_dict, has_key('route_id'))
        assert_that(response_dict, has_key('status'))
        assert_that(response_dict, has_key('passengers'))
        assert_that(response_dict, has_key('amount'))
        assert_that(response_dict, has_key('fee'))



        # 数据正确性断言

        assert_that(response_dict['passengers'], equal_to(5))
        assert_that(response_dict['amount'], equal_to(999))



















