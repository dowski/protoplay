#include <stdio.h>
#include <stdlib.h>
#include "a.pb-c.h"

int
main(int argc, char **argv)
{
    uint8_t *buf, *cur;
    int c, i;
    Request *req;

    buf = calloc(1024, sizeof(uint8_t));
    cur = buf;

    /* 0) Read proto data from stdin. */
    while ((c = getchar()) != EOF) {
        *cur = (char)c;
        cur++;
    }

    /* 1) Unpack the buffer into a Request. */
    req = request__unpack(&protobuf_c_system_allocator, cur - buf - 1, buf);

    if (!req) return 1;

    /* 2) Fill the buffer with junk. We do this to verify the independence
     *    of the buffer and the unpacked Request. */
    for (i=0;i<cur-buf;++i) {
        buf[i] = 'x';
    }

    /* 3) Print out the junk-filled buffer. */
    printf("%s\n", (char *)buf);

    /* 4) Free the buffer so valgrind will tell us if we're touching this
     *    memory later. */
    free(buf);

    /* 5) Access the Request that was unpacked from the buffer - valgrind
     *    should bark at us here if we're touching freed memory. It should
     *    also contain the junk from above if Request just points inside of
     *    the buffer. */
    printf("%s\n", req->payload);

    /* 6) Final cleanup. */
    request__free_unpacked(req, &protobuf_c_system_allocator);

    return 0;
}
