class DynamicArray {

private:

    int* arr;
    int current_size;
    int capacity;

public:

    DynamicArray(int capacity) {
        this->capacity = capacity;
        current_size = 0;
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i]; 
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (current_size == capacity) {
            resize();
        }
        arr[current_size] = n;
        current_size++;
    }

    int popback() {
        current_size--;
        return arr[current_size];
    }

    void resize() {
        this->capacity = this->capacity * 2;
        int* new_array = new int[this->capacity];

        
        for (int i = 0; i < current_size; ++i) {
            new_array[i] = arr[i];
        }

        delete[] arr;
        arr = new_array;

    }

    int getSize() {
        return current_size;
    }

    int getCapacity() {
        return capacity;
    }
};
