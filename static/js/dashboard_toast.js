// const { Toast } = require("bootstrap");

const myToast = new bootstrap.Toast(".toast");

setTimeout(() => {
    myToast.show();
}, 1000);
