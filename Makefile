all: a.pb-c.o
	gcc main.c -o protoplay -I./ -lprotoc -lpthread a.pb-c.o -lprotobuf-c

a.pb-c.o:
	gcc -fPIC -I. -c a.pb-c.c

validate: all
	python gen_a.py | valgrind ./protoplay

clean:
	rm -f protoplay
	rm -f a.pb-c.o
