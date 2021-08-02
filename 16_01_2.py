class Sample:

    def __del__(self):
        print("인스턴스가 소멸됩니다.")

sample = Sample()

del sample #객체가 자동 소멸