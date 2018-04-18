#include <ATen\Context.h>
extern "C" {
    extern THCState *state = at::globalContext().lazyInitCUDA();
}
