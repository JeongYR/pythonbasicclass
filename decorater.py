class Korean:
    country = "korea"

    @classmethod  #클래스메소드
    def trip (cls, country):
        if cls.country == country:
            print("국내여행입니다.")
        else:
            print("해외여행입니다.")

Korean.trip('korea')
Korean.trip('usa')
