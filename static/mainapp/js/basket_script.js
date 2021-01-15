"use strict"

window.onload = function () {
    console.log('DOM is loaded')
    $('.increase').on('click', function (event){
        console.log("target:", event.target)
    })
}