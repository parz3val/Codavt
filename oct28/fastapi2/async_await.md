# Concurency and async/await

Async code just means that the language has a way to tell the program that at some point in the code, it will have to wait for something else to finish somewhere else. Let's say that somethign else is called 'slow-file'

So, during thta time, the computer cna go and do some other work, while 'slow-file' fishes.

Then the program will come back every time it has a chance because it's waiting again, or whenever it finishes all the work it had at that point. And it will ssee if any of the tasks it was waiting for have already finsiehd, doing whatever it had to do.

The "wait for something elsee" refers to I/O operations that are relatively "slow" (compared to the speed of the processor and the RAM memory), like waiting for:

- the data from the client to be sent through the network
- the data sent by your proram to be received by the client through the network
- the contents of a file in the disk to be read by the system and given to the prorgam
- contents of file being written to the disk.
- executing the queries or db ops to finish
- a remote API operation
- and more 

The execution time consumed by waiting for I/O ops is called "I/O bound" ops.

Its called asynchronous because the computer /program doesn't have to 'synchronized' with the slow task, waiting for the exact moment that the task finishes, while doing nothing, to be able to take the task resustl and continue the work.

Inteas of that, beieng "async" system, once finished, the task can wait in line a little bit for the program to finish whatever it went to do, and then come back to take the results and continue working with them.


## TL;DR:
If you are using a library that requires us to call them with `await`, e.g.:

```python
results = await some_library()
```

Then, declare your path operation functions with `async def` like:

```python
@app.get('/')
async def read_results():
    results = await some_library()
    return results
```

>> Note : You can only use `await` inside of functions created using async def.

>> In case of FastAPI, we can mix `async def ` with `def` and FastAPI will figure out what to do.


### Concurency
Concurency is the process of completing tasks concurently, meaning doing multiple tasks at the same time to finish them at the same time.
Suppose I have a task A, that needs time t1 to complete where t1 is not limited to defined value, then concurency is the act of working on task B during t1 to complete A and B at the same time t1. Here during the process of A, I can work on B.

## Parallelism
Parallelsim is the process sof completing tasks at the same time with multiple processes.

>> Conclusion

In the scenerio of tasks, there is a lot of waiting and concurent system provide less waiting time and efficiency in the process.

This is the case for the most of the web applications. Many, many users, but the server is waiting for their not so good connection to send their requests. And then waiting again for the responses from the users to come back. 
This waiting is usually in "microseconds" but even then it all adds up and its a lot of waiting in the end.

Most of the existing popular python frameworks (including Flask and Django) were created before the async features in Python existed. So, the ways they can be deployed support parallel execution and an older form of aync that is not as powerful.

Even though ASGI frameworks were introduced by Django to add support for Websockets, FastAPI has better implementation.

Async speed is what made NodeJS popular (even though NodeJS is not parallel) and is the strength of GO as a porgramming language.

Because you get parallelism and asynchonicity at the same time, we get higher performance with FastAPI that most of the tested NodeJS frameworks and on par with Go, which is a compiled language closer to C. 

#### Is concurency better than parallelism?
Nope ! But on scenerios where it involves a lot of waiting, it is better. 
