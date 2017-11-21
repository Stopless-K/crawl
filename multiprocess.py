from multiprocessing import Process, Queue


class MP(object):
    
    def __init__(self, thread_num, func, args):
        self.thread_num = thread_num
        self.func = func
        self.result = []
        self.args = args
        self.t = [Process(target=self.f, args=(i, self.thread_num, len(self.args))) for i in range(self.thread_num)]
        self.q = Queue()
    
    def f(self, first, step, total):
        print('[OPR] #%d work start..' % first)
        result = []
        for i in range(first, total, step):
            res = self.func(**self.args[i])
            if not res:
                print('[SUC] #%d work done..' % first)
                break
            result.append(res)
        print('[OPR] #%d sending data..' % first)
        self.q.put(result)
        print('[SUC] #%d all done..' % first)


    def work(self):
        for each in self.t:
            each.start()
            
        for i in range(self.thread_num):
            self.result += self.q.get()

        for each in self.t:
            each.join()
        print('[SUC] all process finished..')
        print('[SUC] all work done..')

