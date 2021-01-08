syms th d a alph 

    T = [ cosd(th)      -cosd(alph)*sind(th)     sind(alph)*sind(th)      a*cosd(th)    
          sind(th)      cosd(alph)*cosd(th)      -sind(alph)*cosd(th)     a*sind(th)
          0             sind(alph)              cosd(alph)              d
          0             0                       0                       1];
for i=0:1000 
    
    q01 = randi([0,180]);
    q02 = randi([0,90]);
    q03 = randi([-90,90]);
    q04 = randi([-90,90]);
    d1 = randi([0,260]);
    
   T10 = subs(T,{th,d,a,alph},{q01,225,0,90});             

   T21 = subs(T,{th,d,a,alph},{q02,0,470,0});              
           
   T32 = subs(T,{th,d,a,alph},{q03,0,0,90}); 
   
   T43 = subs(T,{th,d,a,alph},{0,0,d1,-90});
   
   T54 = subs(T,{th,d,a,alph},{q04,0,176,0});

   T_EndEffector = T10*T21*T32*T43*T54;
   
   T__EndEffector = double(T_EndEffector); 
   dataArray = [q01, q02, q03,q04, d1 T__EndEffector(:,4)'];
   writematrix(dataArray, 'trainset.csv', 'WriteMode',"append");
   
end   
