Question 1 of signal

Question 1: By default, Django signals are executed synchronously. 

This means that when a signal is emitted, the receiver (the function connected to the signal) is executed immediately, 
in the same thread as the caller, before control returns to the caller.

Question 2 of signal

Question 2: Do Django signals run in the same thread as the caller?

Answer: Yes, Django signals run in the same thread as the caller by default.

Question 2 of signal

Question 3: By default, do Django signals run in the same database transaction as the caller?

Answer: Yes, Django signals are part of the same database transaction by default. 
If the transaction is rolled back, any changes made by the signal receiver will also be rolled back.
