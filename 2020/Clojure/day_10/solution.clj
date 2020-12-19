(ns day_10.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "10")

(defn get-lines
  "Read in and parse inputs as seq of integers."
  [file]
  (->> file
       slurp
       str/split-lines
       (map read-string)))

(defn calculate-jolt-diff
  "Naive sliding window over a sorted chain. Could be replaced by `reduce`."
  [inputs]
  (let [outlet 0
        built-in (apply max inputs)
        chain (into inputs [outlet built-in])]
    (loop [chain (sort chain)
           one-jolt-diff 0
           three-jolt-diff 0]
      (let [curr (first chain)
            next (second chain)]
        (if-not (and curr next)
          (* one-jolt-diff three-jolt-diff)
          (if (= 1 (- next curr))
            (recur (rest chain) (inc one-jolt-diff) three-jolt-diff)
            (recur (rest chain) one-jolt-diff (inc three-jolt-diff))))))))

(defn part1
  [_]
  (let [inputs (get-lines "day_10/inputs.txt")]
    (calculate-jolt-diff inputs)))

(defn part2
  [_]
  nil)

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
