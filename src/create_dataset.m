syms th d a alph 

    T = [ cosd(th)      -cosd(alph)*sind(th)     sind(alph)*sind(th)      a*cosd(th)    
          sind(th)      cosd(alph)*cosd(th)      -sind(alph)*cosd(th)     a*sind(th)
          0             sind(alph)              cosd(alph)              d
          0             0                       0                       1];
for i=0:1000 
    
    q01 = randi([0,180]);
    q02 = randi([0,90]);
    q03 = randi([0,90]);
    
   T10 = subs(T,{th,d,a,alph},{q01,80.3,0,90});             

   T21 = subs(T,{th,d,a,alph},{q02,0,67.86,0});              
           
   T32 = subs(T,{th,d,a,alph},{q03-90,0,98.31,-90}); 
   
   T43 = subs(T,{th,d,a,alph},{0,23.08,0,0}); 

   T_EndEffector = T10*T21*T32*T43;
   
   T__EndEffector = double(T_EndEffector); 
   dataArray = [q01, q02, q03, T__EndEffector(:,4)'];
   writematrix(dataArray, 'trainset.csv', 'WriteMode',"append");
   
end   
