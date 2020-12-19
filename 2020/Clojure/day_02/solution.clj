(ns day_02.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "02")

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

(defn validate-password-advanced
  "There's a better way using reduce, I'm lazy to write down that one."
  [passwords]
  (loop [count 0
         passwords passwords]
    (if (seq passwords)
      (let [[low high char s] (first passwords)
            ;; covert to char type
            char (first (seq char))
            ;; question is 1-indexed
            low  (dec low)
            high (dec high)]
        (if (and (or (= char (get s low))
                     (= char (get s high)))
                 (not= (get s low)
                       (get s high)))
          (recur (inc count) (rest passwords))
          (recur count (rest passwords))))
      count)))

(defn part1
  [_]
  (let [inputs (get-lines "./day_02/inputs.txt")]
    (validate-password inputs)))

(defn part2
  [_]
  (let [inputs (get-lines "./day_02/inputs.txt")]
    (validate-password-advanced inputs)))

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
