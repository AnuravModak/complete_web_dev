const express=require('express');
const router=express.Router();
const User=require('../models/User');
const bcrypt=require('bcryptjs');
const passport=require('passport');

const { forwardAuthenticated } = require('../config/auth');

// Login Page
router.get('/login', forwardAuthenticated, (req, res) => res.render('login'));

// Register Page
router.get('/register', forwardAuthenticated, (req, res) => res.render('register'));

// register handle
router.post('/register',(req,res)=>{
    const {name,email,password,password2}=req.body;
    let errors=[]

    // checking whether all mandatory fields has been filled or not...
    if (!name||!email||!password||!password2){
        errors.push({msg:"Please fill all the fields"});
    }
    // if passwords  mismatch
    if (password!==password2){
        errors.push({msg:"Password do not match"});
    }
    // if password length is less than 6 characters
    if (password.length<6){
        errors.push({msg:"Password should be atleast 6 characters"});
    }

    // check if u got anyb errors or not
    if (errors.length>0){
        res.render('register',{
            errors,
            name,
            email,
            password,
            password2
        })

    }
    else{
        // if error doesnt exist then....
        User.findOne({email:email})
        .then((user)=>{
            if (user){
                errors.push({msg:"Email already in Use"});
                res.render('register',{
                    errors,
                    name,
                    email,
                    password,
                    password2
                });

            }
            else{
                const newUser=new User({
                    name,
                    email,
                    password,
                    password2
                });
                // newUser.save()
                // console.log(newUser);
                bcrypt.genSalt(10,(err,salt)=>bcrypt.hash(newUser.password,salt,(err,hash)=>{
                    if (err) throw err;
                // else: store password as hash.......

                    newUser.password=hash;
                // save the user

                    newUser.save()
                    .then((user)=>{
                        req.flash('success_msg',"Successfully registered.");
                        res.redirect('/users/login');
                    })
                    .catch(err=>console.log(err))

                }))

            }
        });
        
    }
    

});

// Login Handler
router.post('/login', (req, res, next) => {
    passport.authenticate('local', {
      successRedirect: '/dashboard',
      failureRedirect: '/users/login',
      failureFlash: "Incorrect Credentials"
    })(req, res, next);
  });

// Logout Handler
router.get('/logout', (req, res) => {
    // req.logout();
    // req.flash('success_msg', 'You are logged out');
    // res.redirect('/users/login');

    if (req.session) {
        req.flash('success_msg', 'You are logged out');
        req.logout
        req.session.destroy();
        res.clearCookie('session-id');
        
        res.redirect('/users/login');
      }
  });

module.exports=router;
