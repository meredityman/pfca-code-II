


class TimeCrawler(object):
    def __init__(self, root_path):
        self.root_path = root_path
        print(f"Created Time Crawler {root_path}")

    def info(self):
        print(self.root_path)

    def static_info(value):
        value.info()

def main():
    timecrawler = TimeCrawler("./data")


    timecrawler.info()
    
    TimeCrawler.static_info(timecrawler)



if __name__ == "__main__":
    main()