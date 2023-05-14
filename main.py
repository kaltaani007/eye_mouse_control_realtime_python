import cv2

import mediapipe as mp
import pyautogui as pg

cap = cv2.VideoCapture(0)

screen_w , screen_h = pg.size()

face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)




while True :

    _ , frames = cap.read()
    frame = cv2.flip(frames , 1)



    rgb_frame = cv2.cvtColor(frames , cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)

    landmark_pts = output.multi_face_landmarks
    #print(landmark_pts)

    frame_h , frame_w , _  = frames.shape

    if landmark_pts:

        landmark = landmark_pts[0].landmark
        #print(landmark)

        for  id , l in enumerate(landmark[474:478]):
            x = int(l.x * frame_w)
            y = int(l.y *frame_h)
            cv2.circle(frames , (x , y) , 4, (0 , 255 , 0 ))




            if id == 0:

                screen_x = (screen_w / frame_w) * x
                screen_y = (screen_h / frame_h) * y
                pg.moveTo(screen_x , screen_y )


            print(x, y )


        left = [landmark[145] , landmark[159]]

        for l in left:
            x = int(l.x * frame_w)
            y = int(l.y * frame_h)
            cv2.circle(frames, (x, y), 4, (255, 0 , 0))

        print(left[0].y - left[1].y)

        if left[0].y - left[1].y < 0.02:
            pg.click()
            print("click")
            pg.sleep(1)




    cv2.imshow("Video Capture " , frames)

    #cv2.ishow("lnmarks" , output )


    if cv2.waitKey(1) == ord('q'):
        break

