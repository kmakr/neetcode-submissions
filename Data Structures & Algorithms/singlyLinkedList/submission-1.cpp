class LinkedNode {
    public:
        int value;
        LinkedNode* next;

    LinkedNode(int val) {
            this->value = val;
            next = nullptr;
        };

    
};

class LinkedList {

private:
    LinkedNode* head;
    LinkedNode* tail;

public:
    LinkedList() {
        this->head = new LinkedNode(-1);
        this->tail = head;
    }

    int get(int index) {
        int i = 0;
        LinkedNode* current = head->next;

        while (current != nullptr && i < index) {
            current = current->next;
            i++;
        }

        if (current != nullptr) {
            return current->value;
        }

        return -1;
    }

    void insertHead(int val) {
        LinkedNode* new_node = new LinkedNode(val);
        new_node->next = this->head->next;
        this->head->next = new_node;

        if (new_node->next == nullptr) {
            this->tail = new_node;
        }
        
    }
    
    void insertTail(int val) {
        LinkedNode* node = new LinkedNode(val);
        this->tail->next = node;
        this->tail = node;
        
    }

    bool remove(int index) {

        LinkedNode* current = head;
        int i = 0;

        while (current != nullptr && i < index) {
            current = current -> next;
            i++;
        }

        // check if it is safe to delete
        if (current == nullptr || current->next == nullptr) {
            return false;
        }

        // tail case
        if (current->next == tail) {
            tail = current;
        }

        // remove node
        LinkedNode* delete_node = current->next;
        current->next = current->next->next;
        delete delete_node;

        return true;
        
    }

    vector<int> getValues() {

        // loop through all the linked list
        vector<int> values;
        LinkedNode* curr = head -> next;

        while (curr != nullptr) {
            values.push_back(curr->value);
            curr = curr->next;
        }

        return values;
    }
};
