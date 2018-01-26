from flask import jsonify
from dao.dashboards import DashBoardsDAO


class DashBoardHandler:
    def build_need_dict(self, row):
        result = {}
        if row[0]:
            result['value'] = int(row[0])
        else:
            result['value'] = 0
        result['label'] = 'Need'
        return result

    def build_available_dict(self, row):
        result = {}
        if row[0]:
            result['value'] = int(row[0])
        else:
            result['value'] = 0
        result['label'] = 'Available'
        return result

    def build_available_dictR(self, row):
        result = {}
        if row[0]:
            result['value'] = int(row[0])
        else:
            result['value'] = 0
        result['label'] = 'Available'
        return result


    def build_need_dictR(self, row):
        result = {}
        if row[0]:
            result['available'] = int(row[0])
        else:
            result['available'] = 0
        if row[1]:
            result['need'] = int(row[1])
        else:
            result['need'] = 0
        result['region'] = row[2]
        return result

    def build_region_dict(self, row):
        result = {}
        if row[0]:
            result['value'] = int(row[0])
        else:
            result['value'] = 0
        result['label'] = row[1]
        return result

    def build_theme_availableR(self):
        result = {}
        result['caption'] = 'Available Per Region'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = 'Regions'
        result['yAxisName'] = 'Quantity'
        result['theme'] = 'fint'
        return result

    def build_theme_needR(self):
        result = {}
        result['caption'] = 'Need Per Region'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = 'Regions'
        result['yAxisName'] = 'Quantity'
        result['theme'] = 'fint'
        return result

    def build_theme_available(self):
        result = {}
        result['caption'] = 'Available Today'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = 'Today'
        result['yAxisName'] = 'Quantity'
        return result

    def build_theme_need(self):
        result = {}
        result['caption'] = 'In Need Today'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = 'Today'
        result['yAxisName'] = 'Quantity'
        return result

    def build_theme_match(self):
        result = {}
        result['caption'] = 'Matching between need and available'
        result['subCaption'] = 'Daily'
        result['startingangle'] = '120'
        result['showlabels'] = '0'
        result['showlegend'] = '1'
        result['enablemultislicing'] = '0'
        result['slicingdistance'] = '15'
        result['showpercentvalues'] = '1'
        result['showpercentintooltip'] = '0'
        result['plottooltext'] = '$label percentage : $datavalue'
        result['theme'] = 'fint'
        return result

    def build_theme_matchW(self):
        result = {}
        result['caption'] = 'Matching between need and available'
        result['subCaption'] = 'Weekly'
        result['startingangle'] = '120'
        result['showlabels'] = '0'
        result['showlegend'] = '1'
        result['enablemultislicing'] = '0'
        result['slicingdistance'] = '15'
        result['showpercentvalues'] = '1'
        result['showpercentintooltip'] = '0'
        result['plottooltext'] = '$label percentage : $datavalue'
        result['theme'] = 'fint'
        return result

    def build_theme_matchR(self):
        result = {}
        result['caption'] = 'Matching between need and available'
        result['subCaption'] = 'Daily'
        result['startingangle'] = '120'
        result['showlabels'] = '0'
        result['showlegend'] = '1'
        result['enablemultislicing'] = '0'
        result['slicingdistance'] = '15'
        result['showpercentvalues'] = '1'
        result['showpercentintooltip'] = '0'
        result['plottooltext'] = '$label percentage : $datavalue'
        result['theme'] = 'fint'
        return result

    def build_theme_availableW(self):
        result = {}
        result['caption'] = 'Available Since 7 Days Ago'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = '7 Days'
        result['yAxisName'] = 'Quantity'
        return result

    def build_theme_needW(self):
        result = {}
        result['caption'] = 'In Need For 7 Days'
        result['subCaption'] = 'Resource App'
        result['xAxisName'] = '7 Days'
        result['yAxisName'] = 'Quantity'
        return result

    def getResourcesNeedsDaily(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesNeedsDaily() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_need_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_need(),data=result_list), 200

    def getResourcesAvailablesDaily(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesAvailablesDaily()  # Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_available_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_available(), data=result_list), 200

    def getResourcesMatchesDaily(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesMatchesDaily()  # Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        if len(need_list)==2:
            for row in need_list:
                if(row == need_list[0]):
                    result = self.build_available_dict(row)
                elif (row == need_list[1]):
                    result = self.build_need_dict(row)
                else:
                    result = self.build_need_dict(row)
                result_list.append(result)
        else:
            result = self.build_available_dict(need_list[0])
            result_list.append(result)
            result = self.build_need_dict(need_list[0])
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_match(), data=result_list), 200

    def getResourcesAvailablesWeekly(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesAvailablesWeekly() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_available_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_availableW(),data=result_list), 200

    def getResourcesNeedsWeekly(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesNeedsWeekly() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_need_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_needW(),data=result_list), 200

    def getResourcesMatchesWeekly(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesMatchesWeekly()  # Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        if len(need_list)==2:
            for row in need_list:
                if(row == need_list[0]):
                    result = self.build_available_dict(row)
                elif (row == need_list[1]):
                    result = self.build_need_dict(row)
                else:
                    result = self.build_need_dict(row)
                result_list.append(result)
        else:
            result = self.build_available_dict(need_list[0])
            result_list.append(result)
            result = self.build_need_dict(need_list[0])
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_matchW(), data=result_list), 200


    def getResourcesMatchesByRegion(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesMatchesByRegion() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_need_dictR(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_matchW(),data=result_list), 200

    def getResourcesNeedsByRegion(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesNeedsByRegion() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_needR(),data=result_list), 200

    def getResourcesAvailablesByRegion(self):
        dao = DashBoardsDAO()
        need_list = dao.getResourcesAvailablesByRegion() #Select cid, card_number, security_code, cname, exp_date from Credit_Card
        result_list = []
        for row in need_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error="Result Not Found"), 404
        else:
            return jsonify(chart=self.build_theme_availableR(),data=result_list), 200