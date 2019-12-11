import time

from utils.mysql import *
from static.edu import *
from models.course import Course


class CourseService:
    def __init__(self):
        # 连接数据库
        self.conn = getDatabaseConnection()
        self.cursor = self.conn.cursor()

    def getCourseByCourseId(self, course_id):
        """
            获取课程模型
        :param course_id: 课程id
        :return: 存在返回course对象，否则返回None
        """
        sql = "SELECT * FROM course WHERE id=%s"
        self.cursor.execute(sql, course_id)
        res = self.cursor.fetchall()

        course = None
        err = ErrorCode.NoError
        if len(res) == 0:
            err = ErrorCode.CourseResourceNotFoundError
        else:
            dict = res[0]  # 返回是一个列表，取第一个（也只有一个）
            course = Course(id=str(dict["id"]), name=dict["name"], key=dict["key"],
                            creator_id=str(dict["creator_id"]), create_timestamp=dict["create_timestamp"],
                            status=dict["status"], notice=dict["notice"], introduction=dict["introduction"],
                            joinable=dict["joinable"])
        return course, err

    def getCourseBasicListByUid(self, uid):
        """
            获取课程的基本信息（course_id、 course_name）
            通过用户uid获取用户加入（或创建）的课程的基本信息
        :param uid: 用户id
        :return: 返回列表res，若无课程则为空列表
                 其中元素为字典，keys如下
                 |-dict
                    |-course_id
                    |-course_name
        """
        sql = "SELECT CAST(id AS CHAR) AS course_id, name AS course_name " \
              "FROM course " \
              "WHERE id IN (SELECT course_id FROM join_course WHERE uid=%s)"
        self.cursor.execute(sql, uid)
        res = self.cursor.fetchall()

        return res
