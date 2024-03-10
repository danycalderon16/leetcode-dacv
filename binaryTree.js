class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinaryTree {
  constructor() {
    this.root = null;
  }

  insert(value) {
    const newNode = new Node(value);
    if (!this.root) {
      this.root = newNode;
    } else {
      this.insertNode(this.root, newNode);
    }
  }

  insertNode(root, newNode) {
    if (newNode.value < root.value) {
      if (root.left === null) {
        root.left = newNode;
      } else {
        this.insertNode(root.left, newNode);
      }
    } else {
      if (root.right === null) {
        root.right = newNode;
      } else {
        this.insertNode(root.right, newNode);
      }
    }
  }

  inorden(node = this.root, result = []) {
    if (node !== null) {
      this.inorden(node.left, result);
      result.push(node.value);
      this.inorden(node.right, result);
    }
    return result;
  }

  preorden(node = this.root, result = []) {
    if (node !== null) {
      result.push(node.value);
      this.preorden(node.left, result);
      this.preorden(node.right, result);
    }
    return result;
  }

  postorden(node = this.root, result = []) {
    if (node !== null) {
      this.postorden(node.left, result);
      this.postorden(node.right, result);
      result.push(node.value);
    }
    return result;
  }

  view() {
    return this.root;
  }
}

const bt = new BinaryTree();
bt.insert(5);
bt.insert(4);
bt.insert(7);
bt.insert(9);
bt.insert(1);
bt.insert(10);
bt.insert(6);

console.log(bt.inorden());
console.log(bt.preorden());
console.log(bt.postorden());
