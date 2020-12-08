(ns solution1
  (:require [clojure.string :as str]))


(defn get-lines
  "Read in and parse inputs as seq of vectors."
  [file]
  (letfn [(destruct
           [line]
           (let [[low+high+char s] (str/split line #": ")
                 [low+high char] (str/split low+high+char #" ")
                 [low high] (str/split low+high #"-")]
             [(read-string low) (read-string high) char s]))]
    (->> file
         slurp
         str/split-lines
         (map destruct))))

(defn validate-password
  "There's a better way using reduce, I'm lazy to write down that one."
  [passwords]
  (loop [count 0
         passwords passwords]
    (if (seq passwords)
      (let [[low high char s] (first passwords)
            occur (get (frequencies s) (first (seq char)))]
        (if (and occur (>= occur low) (<= occur high))
          (recur (inc count) (rest passwords))
          (recur count (rest passwords))))
      count)))

(comment
  (let [inputs (get-lines "./day_02/inputs.txt")]
    (validate-password inputs)))


