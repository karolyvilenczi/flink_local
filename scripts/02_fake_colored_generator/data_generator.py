from gen_base import DataFeeder
import multiprocessing

def start_feeder(path, rate):
    feeder = DataFeeder(path, rate)
    feeder.run()

if __name__ == '__main__':

    out_file1 = "/home/kvilenczi/Learn/19_Streaming/flink_local/jobs/data/02_colored_data_live/stream1.csv"
    out_file2 = "/home/kvilenczi/Learn/19_Streaming/flink_local/jobs/data/02_colored_data_live/stream2.csv"

    # Start two feeders with different rates
    feeder1 = multiprocessing.Process(
        target=start_feeder,
        args=(out_file1, 1)  # 2 records per second
    )
    
    feeder2 = multiprocessing.Process(
        target=start_feeder,
        args=(out_file2, 2)  # 5 records per second
    )

    feeder1.start()
    feeder2.start()