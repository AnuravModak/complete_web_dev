const LocalStrategy=require('passport-local').Strategy;
const mongoose=require('mongoose');
const bcrypt=require('bcryptjs');
const User=require('../models/User');

module.exports=function(passport){
    passport.use(
        new LocalStrategy({usernameField:'email'},(email,password,done)=>{
            // now check if email is pre-registered or not
            User.findOne({email:email})
            .then((user)=>{
                if (!user){
                    return done(null,false,{msg:"Email not registered!! Please register and try loggin in :)"})
                }
                else{
                    // now refer todo
                    bcrypt.compare(password,user.password,(err,isMatch)=>{
                        if (err) {
                            throw err;}
                        if (isMatch){
                            return done(null,user);
                        }
                        else{
                            return done(null,false,{msg:"Incorrect Password"})
                            // now as in messages.ejs iam passing message if required or else not msg...

                        }
                    });
                }

            })
            .catch(err=>console.log(err));

        })
    )

    passport.serializeUser((user, done) =>{
        done(null, user.id);
      });
    
      passport.deserializeUser(function(id, done) {
        User.findById(id, (err, user)=> {
          done(err, user);
        });
      });
}