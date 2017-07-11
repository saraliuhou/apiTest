# -*- coding: utf-8 -*-
from cof.http import Http
import api_call.distribute.v02.getAccessToken as getToken
import api_call.distribute.v02.Users as me
import api_call.distribute.v02.routes as routes
import json
import datetime

"""
订单接口类，继承自Http类
"""
class Rides(Http):

    def getAllRides(self, page, perpage):
        """
        根据页数和页单位数获取订单
        :param page:
        :param perpage:
        :return:
        """
        url = "/api/v1/rides"
        body = {
            "page": page,
            "per_page": perpage
        }
        response = self.get(url, body)
        return response

    def getPassengerRidesByUserID(self, userID):
        """
        根据乘客id获取乘客订单
        :param userID:
        :return:
        """
        url = "/api/v1/passengers/" + str(userID) + "/rides"
        response = self.getById(url)
        return response

    def postPassengerOrder(self, phone, passengers, route_id, appointment_time):
        """
        创建司机订单
        :param phone:
        :param password:
        :param passengers:
        :param route_id:
        :param appointment_time:
        :return:
        """
        userID = json.loads(me.getUsers().getMe(phone)['data'])['id']
        userToken = json.loads(getToken.GetAccessToken().getUserToken(phone)['data'])['access_token']
        origin_station = json.loads(routes.Routes().getRouteByID(route_id)['data'])['origin_station']
        destination_station = json.loads(routes.Routes().getRouteByID(route_id)['data'])['destination_station']
        print(origin_station['name'])
        print(destination_station['name'])
        url = "/api/v1/passengers/" + str(userID) + "/rides"
        body = {
            "passengers": passengers,
            "route_id": route_id,
            "route_direction": "ascend",
            "appointment_time": appointment_time,
            "ride_type": "carpooling",
            "origin": origin_station['name'],
            "destination": destination_station['name'],
            "origin_coordinate": "114.029005,22.536604",
            "destination_coordinate": "114.02887,22.609235",
            "confirmed_at": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "access_token": userToken
        }
        response = self.post(url, body)
        print(response)
        return response
    def getDriverOrder(self, userID):
        """
        获取司机订单
        :param userID:
        :return:
        """
        url = "/api/v1/drivers/" + str(userID) + "/rides"
        response = self.getById(url)
        return response

    def getOneRide(self, rideID):
        """
        根据订单id获取订单信息
        :param rideID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)
        response = self.getById(url)
        return response

    # def patchRideById(self, rideId):
    def rideAccept(self, driverID, rideID):
        """
        给司机派单
        :param driverID:
        :param rideID:
        :return:
        """
        url = "/api/v1/drivers/"+str(driverID)+"/rides/accept"
        body = {
            "ride_id": rideID

        }
        response = self.post(url, body)
        return response

    def rideArrive(self, rideID):
        """
        将订单状态设为Arrive
        :param rideID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)+"/arrive"
        body = {

        }
        response = self.post(url, body)
        return response

    def rideInProgress(self, rideID):
        """
        将订单状态设为inprogress
        :param rideID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)+"/progress"
        body = {

        }
        response = self.post(url, body)
        return response

    def rideComplete(self, rideID):
        """
        将订单状态设为complete
        :param rideID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)+"/complete"
        body = {

        }
        response = self.post(url, body)
        return response

    def ridePay(self, rideID):
        """
        将订单状态设为paid
        :param rideID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)+"/payments"
        body = {
            "order_type": "ride"

        }
        response = self.post(url, body)
        return response

    def rideRate(self, rideID, rate):
        """
        评价司机
        :param rideID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)+"/rate"
        body = {
            "rating": rate

        }
        response = self.post(url, body)
        return response

    def rideReassign(self, rideID, reasonID):
        """
        改派订单
        :param rideID:
        :param reasonID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)+"/reassign"
        body = {
            "reassign_reason_id": reasonID
        }
        response = self.post(url, body)
        return response

    def rideExpire(self, rideID):
        """
        使订单过期
        :param rideID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)+"/expire"
        body = {


        }
        response = self.post(url, body)
        return response

    def rideCancelByDriver(self, rideID, reasonID):
        """
        司机取消订单
        :param rideID:
        :param reasonID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)+"/driver_cancel"
        body = {
            "cancel_reason_id": reasonID
        }
        response = self.post(url, body)
        return response
    def rideCancelByPassenger(self, rideID, reasonID):
        """
        乘客取消订单
        :param rideID:
        :param reasonID:
        :return:
        """
        url = "/api/v1/rides/"+str(rideID)+"/passenger_cancel"
        body = {
            "cancel_reason_id": reasonID
        }
        response = self.post(url, body)
        return response

    def rideModified(self, rideID, amount, passengers, phone):
        """
        修改订单
        :param rideID:
        :param amount:
        :param passengers:
        :param phone:
        :return:
        """
        userToken = json.loads(getToken.GetAccessToken().getUserToken(phone)['data'])['access_token']
        url = "/api/v1/rides/"+str(rideID)
        body = {
            "passengers": passengers,
            "status": "appointment",
            "route_id": 6,
            "amount": amount,
            "route_direction": "ascend",
            "ride_type": "carpooling",
            "origin": "h",
            "destination": "h",
            "origin_coordinate": "h",
            "destination_coordinate": "h",
            "access_token": userToken
        }
        response = self.patch(url, body)
        return response

    def deleteRide(self, rideID):
        """
        删除订单
        :param rideID:
        :return:
        """
        userToken = json.loads(getToken.GetAccessToken().getAdminToken("13686483827")['data'])['access_token']
        url = "/api/v1/rides/"+str(rideID)
        body = {
            "access_token": userToken
        }
        response = self.delete(url, body)
        return response




if __name__ == "__main__":
    ridetest = Rides()
    nowTime = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    ridetest.deleteRide(4145)




