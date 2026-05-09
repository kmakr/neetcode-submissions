struct Node {
    int val;
    Node *next, *prev;

    Node(int v) : val(v), next(nullptr), prev(nullptr) {}
};

class Deque {

private:
    Node* sentinel;
public:
    Deque() {
        sentinel = new Node(-1);
    }

    bool isEmpty() {
        if (sentinel->next == nullptr) {
            return true;
        }
            
        return false;
    }

    void append(int value) {
        Node* node = sentinel;
        while (node->next != nullptr) {
            node = node->next;
        }
        Node* new_node = new Node(value);
        new_node->prev = node;
        node->next = new_node;
    }

    void appendleft(int value) {
  
        Node* node = sentinel;
        Node* new_node = new Node(value);
        Node* temp = node->next;
        node->next = new_node;
        new_node->prev = node;
        new_node->next = temp;
        

        if (temp != nullptr) {
            temp->prev = new_node;
        }
            
        
    }

    int pop() {
        if (isEmpty()) {
            return -1;
        }
        Node* node = sentinel;
        while (node->next != nullptr) {
            node = node->next;
        }

        int val = node->val;
        node->prev->next = nullptr;
       
        delete node;
        return val;

       
    }

    int popleft() {
        Node* node = sentinel;

        if (isEmpty()) {
            return -1;
        }

        Node* remove = node->next;
        int val = remove->val;
        node->next = remove->next;

        if (remove->next != nullptr) {
            remove->next->prev = node;
            
        }
        delete remove;
        return val;
      
    }
};
