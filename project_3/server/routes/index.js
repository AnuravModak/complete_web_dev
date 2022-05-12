const express=require('express');
const router=express.Router();
const {ensureAuthenticated}=require('../config/auth');


// welcome
router.get('/',(req,res)=>{
    res.statusCode=200;
    res.render('welcome');
})

// dashboard
router.get('/dashboard',ensureAuthenticated,(req,res)=>{
    res.statusCode=200;
    // so from here i will take user and display it in my dashboard....
    res.render('dashboard',{
        name:req.user.name
    });
})




module.exports=router;