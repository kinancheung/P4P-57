struct elem {
  struct elem *prev;
  struct elem *next;
};

#define ELEM_INITIALIZER(NAME) { .prev = &(NAME), .next = &(NAME), }

struct head {
  struct elem header;
};

#define HEAD_INITIALIZER(NAME) { .header = ELEM_INITIALIZER(NAME.header) }

int main(int argc, char ** argv) {
  struct head myhead = HEAD_INITIALIZER(myhead);
}