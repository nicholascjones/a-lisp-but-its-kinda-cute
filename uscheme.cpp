// uscheme.cpp

#include <iostream>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
using namespace std;

// Globals ---------------------------------------------------------------------

bool BATCH = false;
bool DEBUG = false;

// Structures ------------------------------------------------------------------

struct Node {
    Node(string value, Node *left=nullptr, Node *right=nullptr);
    ~Node();

    string value;
    Node * left;
    Node * right;

    friend ostream &operator<<(ostream &os, const Node &n);
};
//constructor
Node::Node(string valuei, Node *lefti, Node *righti){
    value = valuei;
    left = lefti;
    right = righti;
}
//deconstructor
Node::~Node(){
    delete left;
    delete right;
}
//recrusive function to traverse the heap and print values
void  dfs_recursive(ostream &os , const Node &root)
{
    os << "(Node: value= " << root.value << ", ";
    if (root.left){  dfs_recursive(os, *root.left);
    os << "left = " << root.left->value << ", ";}
    if (root.right){ dfs_recursive(os, *root.right);
    os << "right = " << root.right->value << ", ";}
    os << ")";

  return;
}
//printing out the tree traversal
ostream &operator<<(ostream &os, const Node &n) {
  
    dfs_recursive(os, n);
    
      return os;
}

// Parser ----------------------------------------------------------------------

string parse_token(istream &s) {

    string token;
    //skip white space
    
    while (isspace(s.peek()))
    {
        s.get(); //wash
    }
   
    if ((s.peek() == ')') || (s.peek() == '(')) //s is a parenthesis or operator
    {
        token = s.get(); //take token
    }
    else if ((s.peek() == '+') || (s.peek() == '-') || (s.peek() == '/') || (s.peek() == '*'))
    {
        token = s.get();
    } 
    else if (isdigit(s.peek()))//s is a number
    {
        token = s.get();
    }

    return token;
}

Node *parse_expression(istream &s) {

    string token;

    Node * right = nullptr;

    Node * left = nullptr;

    token = parse_token(s);

    if ((token == " ") | (token == ")"))
    {
        return nullptr;       
    }
    if (token == "(")
    {
        token = parse_token(s);
        left = parse_expression(s);
        if (left)
        {
            right =  parse_expression(s);
        }
        if (right)
        {
            parse_token(s);
        }

    }
    //cout << token<< endl;
    //cout << left->value << endl;
    //cout << right->value << endl;
    return new Node(token, left, right); 
}

// Interpreter -----------------------------------------------------------------
//implements stack machine to evaluate the tree as it traverses it
void evaluate_r(const Node *n, stack<int> &s) {
    int val=0;
    if(n->right){
        evaluate_r(n->right, s);
    }
    if(n->left){
        evaluate_r(n->left, s);
    }

    if (isdigit((n->value)[0]))
    {
        s.push(stoi(n->value));
    }
    else
    {
        val = s.top();
        s.pop();
        if (n->value == "+")
        {
            val = val + s.top();
            s.pop();

            s.push(val);
        }        
        else if (n->value == "-")
        {
            val =  val-s.top();
            s.pop();
            s.push(val);
 
        }
        else if (n->value == "/")
        {
            val = val/s.top();
            s.pop();
            s.push(val);
 
        }
        else if (n->value == "*")
        {
            val = val * s.top();
            s.pop();
            s.push(val);
 
        }

    }
   
}

int evaluate(const Node *n) {
 
    stack<int> s; //initialize stack
    evaluate_r(n, s);

   return s.top();
}

// Main execution --------------------------------------------------------------

int main(int argc, char *argv[]) {
    string line;
    int c;

    while ((c = getopt(argc, argv, "bdh")) != -1) {
        switch (c) {
            case 'b': BATCH = true; break;
            case 'd': DEBUG = true; break;
            default:
                cerr << "usage: " << argv[0] << endl;
                cerr << "    -b Batch mode (disable prompt)"   << endl;
                cerr << "    -d Debug mode (display messages)" << endl;
                return 1;
        }
    }
    //read in process, parsing, and evaulation begins
    while (!cin.eof()) {
        if (!BATCH) {
            cout << ">>> ";
            cout.flush();
        }

        if (!getline(cin, line)) {
            break;
        }

        if (DEBUG) { cout << "LINE: " << line << endl; }

        stringstream s(line);
        Node *n = parse_expression(s);
        if (DEBUG) { cout << "TREE: " << *n << endl; }

        cout << evaluate(n) << endl;

        delete n;
    }

    return 0;
}

// vim: set sts=4 sw=4 ts=8 expandtab ft=cpp:
