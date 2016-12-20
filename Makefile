CC=txt2tags
T2T=$(wildcard *.t2t)
MAN=$(T2T:.t2t=.man)

all: $(MAN)

%.man: %.t2t
	$(CC) -o - $< | soelim | preconv -eutf8 > $@

clean:
	rm -f *.man *~
