class Course:
    def __init__(self, id=None, name=None, key=None, creator_id=None, create_timestamp=None, status=None, notice=None,
                 introduction=None, joinable=None):
        self.id = id  # 课程唯一标识
        self.name = name  # 课程名
        self.key = key  # 选课码
        self.creator_id = creator_id  # 课程创建人唯一标识
        self.create_timestamp = create_timestamp  # 课程创建时间
        self.status = status  # 课程状态
        self.notice = notice  # 课程介绍
        self.introduction = introduction  # 课程公告
        self.joinable = joinable  # 是否可以加入
