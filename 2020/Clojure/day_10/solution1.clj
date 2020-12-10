(ns solution1
  (:require [clojure.string :as str]))

(defn get-lines
  "Read in inputs as seq of integers."
  [file]
  (map read-string (str/split-lines (slurp file))))

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

(comment
  (let [inputs (get-lines "day_10/inputs.txt")]
    (calculate-jolt-diff inputs)))
