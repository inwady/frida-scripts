Java.perform(function () {
    var target = Java.use('<class_name>');

    target.setItem.implementation = function (v1, v2, v3, v4, v5) {
       console.log(v1, v2, v3, v4, v5);
    };
});

