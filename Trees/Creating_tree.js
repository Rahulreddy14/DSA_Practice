class Node {
    constructor(val){
        this.val = val ;
        this.left = null;
        this.right = null ;

    }
}

// breadth first search

const breadthFirstValues = (root) => {
    if(root === null ) return  []

    const values = []

    const queue = [ root ];

    while (queue.length > 0 ) {
       const current =  queue.shift();
       values.push(current.val)

       if(current.left !== null) queue.push(current.left);
       if(current.left !== null) queue.push(current.right);
    }

    return values; 
}

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

values_1 = breadthFirstValues(a)

console.log(values_1);