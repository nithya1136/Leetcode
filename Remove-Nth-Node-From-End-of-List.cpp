/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int length(ListNode* head){
        ListNode * cn=head;
        int c=0;
        while(cn!=NULL){
            cn=cn->next;
            c++;
        }
        return c;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode * cn=head;
        int l=length(head);
        int c=0;
        if (n==l) {
            return head->next;
        }
        while(c<l-n-1){
            cn=cn->next;
            c++;
        }
        if (cn->next != NULL) {
            cn->next = cn->next->next;
        }
        return head;
    }
};